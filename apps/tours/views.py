from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action

from .models import Tour
from .serializers import ReviewSerializer, TourSerializer, LikeSerializer
from rest_framework.response import Response


class TourViewSet(viewsets.ModelViewSet):
    queryset = Tour.objects.all()

    def get_permissions(self):
        if self.action in ('review', 'like'):
            return [permissions.IsAuthenticated()]
        elif self.request.method in ('POST', 'PUT', 'PATCH', 'DELETE'):
            return [permissions.IsAdminUser()]
        return [permissions.AllowAny()]

    def get_serializer_class(self):
        if self.action == 'review':
            return ReviewSerializer
        if self.action == 'like':
            return LikeSerializer
        return TourSerializer

    @action(['POST'], detail=True)
    def review(self, request, pk=None):
        tour = self.get_object()
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(tour=tour, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(['POST'], detail=True)
    def like(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
