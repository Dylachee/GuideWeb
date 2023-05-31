from django.urls import path
from .views import (TraditionalClothingList, 
                    TraditionalClothingRetrieveUpdateDestroyAPIView,
                    TraditionalSSouvenirsList,
                    TraditionalSSouvenirsRetrieveUpdateDestroyAPIView)

urlpatterns = [
     path('traditional-clothing/', TraditionalClothingList.as_view(), 
         name='traditional-clothing-list'),
     path('traditional-clothing/<int:pk>/', TraditionalClothingRetrieveUpdateDestroyAPIView.as_view(), 
         name='traditional-clothing-detail'),
     path('traditional-souvenirs' , TraditionalClothingList.as_view(), 
          name='traditional-souvenirs'),
     path('traditional-souvenirs/<int:pk>/', TraditionalClothingRetrieveUpdateDestroyAPIView.as_view(),
          name = 'traditional-souvenirs-detail'),
]
