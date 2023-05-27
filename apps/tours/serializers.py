from rest_framework import serializers

from .models import Tour, Review, Like


class TourListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        return super().to_representation(data)


class TourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tour
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('tour', 'user')

    def validate(self, attrs):
        user = self.context['request'].user
        tour = self.context['view'].get_object()
        if Review.objects.filter(tour=tour, user=user).exists():
            raise serializers.ValidationError('You already reviewed this tour')
        return attrs


class LikeSerializer(serializers.Serializer):
    user = serializers.IntegerField(read_only=True)

    def validate(self, attrs):
        user = self.context['request'].user
        tour = self.context['view'].get_object()
        if Like.objects.filter(tour=tour, user=user).exists():
            Like.objects.filter(tour=tour, user=user).delete()
            attrs['liked'] = False
        else:
            Like.objects.create(user=user, tour=tour)
            attrs['liked'] = True
        return attrs
