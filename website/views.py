from django.shortcuts import render, get_object_or_404
from .models import Dish

# Create your views here.
def home(request):
    dishes = Dish.objects.all()
    return render(request, 'website/home.html', {'dishes': dishes})

def dish_detail(request, pk):
    dish = Dish.objects.get(pk=pk)
    return render(request, 'website/dish_detail.html', {'dish': dish})
