from rest_framework import generics ,status
from .models import TraditionalClothing
from .serializers import TraditionalClothingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class TraditionalClothingList(generics.ListCreateAPIView):
    queryset = TraditionalClothing.objects.all()
    serializer_class = TraditionalClothingSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = TraditionalClothingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TraditionalClothingRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TraditionalClothing.objects.all()
    serializer_class = TraditionalClothingSerializer
    permission_classes = [IsAuthenticated]