from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CustomUserViewSet

router = DefaultRouter()
router.register('user', CustomUserViewSet, 'user')

urlpatterns = [
    path('', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
