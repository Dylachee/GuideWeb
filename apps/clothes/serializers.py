from rest_framework import serializers
from .models import TraditionalClothing

class TraditionalClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TraditionalClothing
        fields = '__all__'
