from django.shortcuts import render, get_object_or_404
from .models import Dish, Restaurant, Review
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    dishes = Dish.objects.all()
    return render(request, 'website/home.html', {'dishes': dishes})

def dish_detail(request, pk):
    dish = Dish.objects.get(pk=pk)
    reviews = Review.objects.filter(dish=dish)
    dishes = Dish.objects.filter(restaurant = dish.restaurant)
    return render(request, 'website/dish_detail.html', {'dish': dish, 'reviews':reviews, 'dishes':dishes})

def user_detail(request, pk):
    user = User.objects.get(pk=pk)
    reviews = Review.objects.filter(author=user)
    return render(request, 'website/user_detail.html', {'user': user, 'reviews':reviews,})
