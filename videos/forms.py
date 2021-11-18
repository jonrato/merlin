from django import forms  
from .models import Cursos 
 
class PostForm(forms.ModelForm):  
    class Meta:  
        model = Cursos  
        fields = ['title', 'description', 'link',
                'image'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'title': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'description': forms.TextInput(attrs={ 'class': 'form-control' }),
            'link': forms.TextInput(attrs={ 'class': 'form-control' }),
            'image': forms.FileInput(attrs={ 'class': 'form-control' }),
      }
