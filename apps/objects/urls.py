from django.urls import path
from .views import (TraditionalFoodAPIView, 
                    TraditionalFoodDetailAPIView,
                    CategoryListCreateAPIView,
                    CategoryRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('food/', TraditionalFoodAPIView.as_view(), name='food_list'),
    path('food/<int:pk>/', TraditionalFoodDetailAPIView.as_view(), name='food_detail'),
    path('category/', CategoryListCreateAPIView.as_view(), name='category_list_create'),
    path('category/<int:pk>/', CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category_retrieve_update_destroy'),
]

