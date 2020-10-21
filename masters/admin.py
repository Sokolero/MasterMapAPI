from django.contrib import admin
from .models import Category, Master, MasterObject, Location, Photo
# from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Category)
admin.site.register(Master)
admin.site.register(MasterObject)
admin.site.register(Location)
admin.site.register(Photo)
