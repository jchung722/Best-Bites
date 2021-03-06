from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Review, Dish, Restaurant


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ('rating', 'feedback',)

class DishForm(forms.ModelForm):

    class Meta:
        model = Dish
        fields = ('name', 'image', 'price', 'description')

class RestaurantForm(forms.ModelForm):

    class Meta:
        model = Restaurant
        fields = ('name', 'image', 'location', 'phone', 'website')
