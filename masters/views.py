from django.contrib.auth.models import User#model from built-in system auth of django
from .serializers import (UserSerializer, MasterSerializer,
 CategorySerializer, MasterObjectSerializer,
 LocationSerializer, PhotoSerializer)
from django.shortcuts import get_object_or_404
from .models import Master, Category, MasterObject, Location, Photo

from rest_framework.response import Response
from rest_framework import viewsets

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class MasterViewSet(viewsets.ModelViewSet):
    queryset = Master.objects.all()
    serializer_class = MasterSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class MasterObjectViewSet(viewsets.ModelViewSet):
    queryset = MasterObject.objects.all()
    serializer_class = MasterObjectSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    # def retrieve(self, request, pk=None):
    #     queryset = self.get_queryset()
    #     user  = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)

    # def create(self, request):
    #     queryset = self.get_queryset()
    #     serializer = UserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)

    # def update(self, request, pk=None):
    #     queryset = self.get_queryset()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = UserSerializer(user, data=request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #
    # def destroy(self, request, pk=None):
    #     queryset = self.get_queryset()
    #     user = get_object_or_404(queryset, pk=pk)
    #     user.delete()
    #     return Response({ "status": "deleted" })
