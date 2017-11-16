from django.contrib import admin
from .models import Dish, Restaurant, Review

myModels = [Dish, Restaurant, Review]
admin.site.register(myModels)
