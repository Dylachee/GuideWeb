from rest_framework import generics
from .models import TraditionalFood , Category , Cart , Order
from .serializers import (TraditionalFoodSerializer , 
                          CategorySerializer ,
                            CartSerializer , 
                            OrderSerializer)

from rest_framework.permissions import IsAuthenticated
class TraditionalFoodAPIView(generics.ListCreateAPIView):
    queryset = TraditionalFood.objects.all()
    serializer_class = TraditionalFoodSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class TraditionalFoodDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TraditionalFood.objects.all()
    serializer_class = TraditionalFoodSerializer
    permission_classes = [IsAuthenticated]

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class CartListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

class CartRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]