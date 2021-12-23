from django import forms
from django.contrib.contenttypes import fields
from django.forms import widgets
from django_app.models import Comment_Assinaturas

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Insira seu comentário',
        'rows':'4',
    }))

    class Meta:
        model  = Comment_Assinaturas
        fields = ('content',)


from django import forms  
from .models import Cursos  
class CursosForm(forms.ModelForm):  
    class Meta:  
        model = Cursos  
        fields = ['titulo', 'professor', 'preco',
                'parcela', 'link', 'imagem'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'titlulo': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'professor': forms.TextInput(attrs={ 'class': 'form-control' }),
            'preco': forms.TextInput(attrs={ 'class': 'form-control' }),
            'parcela': forms.TextInput(attrs={ 'class': 'form-control' }),
            'link': forms.TextInput(attrs={ 'class': 'form-control' }),
            'imagem': forms.FileInput(attrs={ 'class': 'form-control' }),
      }

from .models import Post_Assinaturas
class AssinaturaForm(forms.ModelForm):
    class Meta:
        model = Post_Assinaturas
        fields = [
            'title', 'images','overview', 'content', 'author', 'categories'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'images': forms.FileInput(attrs={'class':'form-control'}),
            'overview': forms.TextInput(attrs={'class':'form-control'}),
            'content': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control'}),
            'categories': forms.TextInput(attrs={'class':'form-control'}),
        }


