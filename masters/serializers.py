from rest_framework import serializers
from datetime import date

from django.contrib.auth.models import User
from .models import Master, Category, MasterObject, Location, Photo

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'username', 'password', 'email', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}


class MasterSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    categorys = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), many=True)
    class Meta:
        model = Master
        fields = ['pk', 'phone', 'user', 'categorys']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'category_name']
        read_only = ['pk', 'category_name']


class MasterObjectSerializer(serializers.ModelSerializer):
    location = serializers.PrimaryKeyRelatedField(queryset=Location.objects.all())
    master = serializers.PrimaryKeyRelatedField(queryset=Master.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = MasterObject
        fields = ['pk', 'location', 'master', 'category']


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['pk', 'coordX', 'coordY']


class PhotoSerializer(serializers.ModelSerializer):
    master_object = serializers.PrimaryKeyRelatedField(queryset=MasterObject.objects.all())
    class Meta:
        model = Photo
        fields = ['pk', 'image', 'master_object']
# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=32)
#     password = serializers.CharField(max_length=32)
#     email = serializers.EmailField(max_length=32)
#     first_name = serializers.CharField(max_length=32)
#     last_name = serializers.CharField(max_length=32)
#
#     def create(self, validated_data):
#         return User.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
        # instance.username = validated_data.get('username', instance.username)
#         instance.password = validated_data.get('password', instance.password)
#         instance.email = validated_data.get('email', instance.email)
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.save()
#         return instance
