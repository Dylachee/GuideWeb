from django.urls import path
from .views import (TraditionalClothingList, 
                    TraditionalClothingRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('traditional-clothing/', TraditionalClothingList.as_view(), 
         name='traditional-clothing-list'),
    path('traditional-clothing/<int:pk>/', TraditionalClothingRetrieveUpdateDestroyAPIView.as_view(), 
         name='traditional-clothing-detail'),
]
