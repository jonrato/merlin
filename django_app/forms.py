from django import forms
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
