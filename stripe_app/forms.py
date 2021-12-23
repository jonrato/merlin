from django import forms
from .models import Icecream, Size
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class IceForm(forms.ModelForm):
    class Meta:
        model = Icecream
        fields = ['topping1','topping2','size']
        labels = {'topping1': 'Topping 1','topping2': 'Topping 2'}

class MultipleIceForm(forms.Form):
    numofice = forms.IntegerField(min_value=2,max_value=10)

class CustomSignupForm(UserCreationForm):
    email = forms.EmailField(max_length=255, required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')