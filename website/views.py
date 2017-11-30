from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Dish, Restaurant, Review
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import SignUpForm, ReviewForm, DishForm, RestaurantForm
from django.db.models import Avg

# Create your views here.
def home(request):
    dishes = Dish.objects.all()
    return render(request, 'website/home.html', {'dishes': dishes})

def dish_detail(request, pk):
    dish = Dish.objects.get(pk=pk)
    reviews = dish.reviews.all()

    dishes = Dish.objects.filter(restaurant = dish.restaurant)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.dish = dish
            review.created_date = timezone.now()
            review.save()
            return redirect('dish_detail', pk=dish.pk)
    else:
        form = ReviewForm()
        return render(request, 'website/dish_detail.html', {'form':form, 'dish':dish, 'reviews':reviews, 'dishes':dishes})

def restaurant_detail(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    dishes = Dish.objects.filter(restaurant = restaurant)
    return render(request, 'website/restaurant_detail.html', {'restaurant':restaurant, 'dishes':dishes,})

def user_detail(request, pk):
    user = User.objects.get(pk=pk)
    reviews = Review.objects.filter(author=user)
    return render(request, 'website/user_detail.html', {'user': user, 'reviews':reviews,})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'website/signup.html', {'form': form})

def dish_list(request):
    dishes = Dish.objects.all()
    query = request.GET.get("q")
    if query:
        dishes = dishes.filter(name__icontains=query)
    return render(request, 'website/dish_list.html', {'dishes': dishes})

def dish_new(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    if request.method == "POST":
        form = DishForm(request.POST)
        if form.is_valid():
            dish = form.save(commit=False)
            dish.restaurant = restaurant
            dish.save()
            return redirect('restaurant_detail', pk=restaurant.pk)
    else:
        form = DishForm()
    return render(request, 'website/dish_new.html', {'form': form})

def restaurant_new(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            restaurant = form.save(commit=False)
            restaurant.save()
            return redirect('restaurant_detail', pk=restaurant.pk)
    else:
        form = RestaurantForm()
    return render(request, 'website/restaurant_new.html', {'form': form})
