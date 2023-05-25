from rest_framework import serializers
from .models import TraditionalFood, Category

class TraditionalFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TraditionalFood
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'