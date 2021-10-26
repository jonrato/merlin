from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from userprofile.models import Profile


class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'size':'50rem',
            'required':'',
            'name':'username',
            'type': 'text',
            'class': 'text-center',
            'placeholder': 'digite seu nome de usuario',
            'maxlength':'50',
            'minlength': '5'
        })
        self.fields["email"].widget.attrs.update({
            'size':'50rem',
            'required':'',
            'name':'email',
            'type': 'email',
            'class': 'text-center',
            'placeholder': 'digite seu email',
            
        })
        self.fields["first_name"].widget.attrs.update({
            'size':'50rem',
            'required':'',
            'name':'first_name',
            'type': 'text',
            'class': 'text-center',
            'placeholder': 'Digite seu primeiro nome',
            'maxlength':'50',
            'minlength': '5'
        })
        self.fields["last_name"].widget.attrs.update({
            'size':'50rem',
            'required':'',
            'name':'last_name',
            'type': 'text',
            'class': 'text-center',
            'placeholder': 'digite seu sobrenome',
            'maxlength':'50',
            'minlength': '5'
        })
        self.fields["password1"].widget.attrs.update({
            'size':'50rem',
            'required':'',
            'name':'password1',
            'type': 'password',
            'class': 'text-center',
            'placeholder': 'digite sua sennha',
            'maxlength':'50',
            'minlength': '8'
        })
        self.fields["password2"].widget.attrs.update({
            'size':'50rem',
            'required':'',
            'name':'password2',
            'type': 'password',
            'class': 'text-center',
            'placeholder': 'confirme sua senha',
            'maxlength':'50',
            'minlength': '8'
        })
        
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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            'size':'50rem',
            'required':'',
            'name':'username',
            'type': 'text',
            'class': 'text-center',
            'placeholder': 'nome de usuario',
            'maxlength':'50',
            'minlength': '5'
        })
        self.fields["first_name"].widget.attrs.update({
            'size':'50rem',
            'required':'',
            'name':'first_name',
            'type': 'text',
            'class': 'text-center',
            'placeholder': 'Seu Nome',
            'maxlength':'50',
            'minlength': '5'
        })

        self.fields["last_name"].widget.attrs.update({
            'size':'50rem',
            'required':'',
            'name':'last_name',
            'type': 'text',
            'class': 'text-center',
            'placeholder': 'Seu Sobrenome',
            'maxlength':'50',
            'minlength': '5'
        })
        self.fields["email"].widget.attrs.update({
            'size':'50rem',
            'required':'',
            'name':'email',
            'type': 'text',
            'class': 'text-center',
            'placeholder': 'Seu Email',
            'maxlength':'50',
            'minlength': '5'
        })
        
    class Meta:
        model = User
        fields = [
            'username',
            'first_name', 
            'last_name',
            'email',
            

        ]

class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["telefone"].widget.attrs.update({
            'size':'50rem',
            'required':'',
            'name':'telefone',
            'type': 'text',
            'class': 'text-center',
            'placeholder': 'Seu Telefone',
            'maxlength':'50',
            'minlength': '5'
        })
        self.fields["cidade"].widget.attrs.update({
            'size':'50rem',
            'required':'',
            'name':'cidade',
            'type': 'text',
            'class': 'text-center',
            'placeholder': 'Sua Cidade',
            'maxlength':'50',
            'minlength': '5'
        })

        self.fields["estado"].widget.attrs.update({
            'size':'50rem',
            'required':'',
            'name':'estado',
            'type': 'text',
            'class': 'text-center',
            'placeholder': 'Estado',
            'maxlength':'50',
            'minlength': '5'
        })
        self.fields["profile_image"].widget.attrs.update({
            'size':'50rem',
            'name':'profile_image',
            'type': 'text',
            'class': 'text-center',
            'placeholder': 'Imagem de Perfil',
            'maxlength':'50',
            'minlength': '5'
        })
    class Meta:
        model = Profile
        fields = [
            'telefone',
            'cidade',
            'estado',
            'profile_image',
        ]