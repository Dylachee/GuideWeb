from rest_framework import serializers
from .models import TraditionalClothing , TraditionalSouvenirs

class TraditionalClothingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TraditionalClothing
        fields = '__all__'

class TraditionalSuvenirsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TraditionalClothing
        fields = '__all__'