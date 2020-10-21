from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=32)
    def __str__(self):
        return self.category_name

class Master(models.Model):
    phone = models.CharField(max_length=32)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    categorys = models.ManyToManyField(Category)

class Location(models.Model):
    coordX = models.FloatField()
    coordY = models.FloatField()

class MasterObject(models.Model):
    location = models.OneToOneField(Location, on_delete=models.CASCADE)
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)


class Photo(models.Model):
    image = models.ImageField()
    master_object = models.ForeignKey(MasterObject, on_delete=models.CASCADE)
