from django.urls import path
from .views import (UserViewSet, MasterViewSet, CategoryViewSet,
    MasterObjectViewSet, LocationViewSet, PhotoViewSet)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'masters', MasterViewSet, basename='master')
router.register(r'categorys', CategoryViewSet, basename='category')
router.register(r'objects', MasterObjectViewSet, basename='object')
router.register(r'locations', LocationViewSet, basename='location')
router.register(r'photos', PhotoViewSet, basename='photo')

urlpatterns = router.urls
