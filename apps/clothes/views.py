from rest_framework import generics ,status
from .models import TraditionalClothing , TraditionalSouvenirs
from .serializers import TraditionalClothingSerializer , TraditionalSuvenirsSerializer
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

class TraditionalSSouvenirsList(generics.ListCreateAPIView):
    queryset = TraditionalSouvenirs.objects.all()
    serializer_class = TraditionalSuvenirsSerializer
    permission_classes = [IsAuthenticated]

class TraditionalSSouvenirsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TraditionalSouvenirs.objects.all()
    serializer_class = TraditionalSuvenirsSerializer
    permission_classes = [IsAuthenticated]