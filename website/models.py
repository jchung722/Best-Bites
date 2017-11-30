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

    @property
    def average_rating(self):
        total = 0
        count = 0
        average = 0
        reviews = self.reviews.all()
        for review in reviews:
            total += int(review.rating)
            count += 1

        if total > 0:
            average = float("{0:.1f}".format(total/count))

        return average

    def average_rating_range(self):
        average_int = int(self.average_rating)
        return range(0, average_int)

    pass

class Review(models.Model):
    author = models.ForeignKey('auth.User')
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='reviews')
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

    def rating_range(self):
        rating_int = int(self.rating)
        return range(0, rating_int)
