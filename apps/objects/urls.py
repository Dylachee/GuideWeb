from django.urls import path
from .views import (TraditionalFoodAPIView, 
                    TraditionalFoodDetailAPIView,
                    CategoryListCreateAPIView,
                    CategoryRetrieveUpdateDestroyAPIView,
                    CartListCreateAPIView,
                    CartRetrieveUpdateDestroyAPIView,
                    OrderListCreateAPIView,
                    OrderRetrieveUpdateDestroyAPIView,
                    )

urlpatterns = [
    path('api/food/', TraditionalFoodAPIView.as_view(), name='food_list'),
    path('api/food/<int:pk>/', TraditionalFoodDetailAPIView.as_view(), name='food_detail'),
    path('api/category/', CategoryListCreateAPIView.as_view(), name='category_list_create'),
    path('api/category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), 
         name='category_retrieve_update_destroy'),
    path('api/cart/', CartListCreateAPIView.as_view(), name='food_cart_list_create'),
    path('api/cart/<int:pk>/', CartRetrieveUpdateDestroyAPIView.as_view(), 
         name='food_cart_retrieve_update_destroy'),
    path('api/orders/', OrderListCreateAPIView.as_view(), 
         name='food_order_list_create'),
    path('api/orders/<int:pk>/', OrderRetrieveUpdateDestroyAPIView.as_view(), 
         name='food_order_retrieve_update_destroy'),
]









