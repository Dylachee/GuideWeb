from rest_framework import generics
from .models import TraditionalClothing
from .serializers import TraditionalClothingSerializer
from rest_framework.permissions import IsAuthenticated

class TraditionalClothingList(generics.ListAPIView):
    queryset = TraditionalClothing.objects.all()
    serializer_class = TraditionalClothingSerializer
    permission_classes = [IsAuthenticated]

class TraditionalClothingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TraditionalClothing.objects.all()
    serializer_class = TraditionalClothingSerializer
    permission_classes = [IsAuthenticated]
