from django.db import models
from django.utils import timezone


# Create your models here.
class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    website = models.URLField(max_length=200)
    image = models.CharField(max_length=200)
    pass

class Dish(models.Model):
    name = models.CharField(max_length=200)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    image = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    description = models.TextField()
    pass

class Review(models.Model):
    author = models.ForeignKey('auth.User')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    RATING = (
        ('5', '5 - The best!'),
        ('4', '4 - Delicious!'),
        ('3', '3 - Okay'),
        ('2', '2 - Subpar'),
        ('1', '1 - A no from me')
    )
    rating = models.CharField(
        max_length=1,
        choices=RATING,
        default=5,
    )
    feedback = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
