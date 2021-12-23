from django import forms  
from videos.models import Post
from django import forms
from django.contrib.contenttypes import fields
from django.forms import widgets
 
class PostForm(forms.ModelForm):  
    class Meta:  
        model = Post  
        fields = ['title', 'description', 'link',
                'image'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'title': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'description': forms.TextInput(attrs={ 'class': 'form-control' }),
            'link': forms.TextInput(attrs={ 'class': 'form-control' }),
            'image': forms.FileInput(attrs={ 'class': 'form-control' }),
      }
