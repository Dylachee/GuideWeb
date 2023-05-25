from rest_framework import serializers
from .models import TraditionalFood, Category , Cart , Order

class TraditionalFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TraditionalFood
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'