from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from userprofile.models import Profile


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=50, required=False, help_text='Optional1')
    last_name = forms.CharField(max_length=50, required=False, help_text='Optional1')
    email = forms.EmailField(max_length=100, help_text="Insira um endereco de email valido")

    class Meta:
        model = User
        fields = [
            'username',
            'first_name', 
            'last_name',
            'email',
            'password1',
            'password2',
        ]

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name', 
            'last_name',
            'email',

        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'cidade',
            'estado',
            'profile_image'
        ]