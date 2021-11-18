from django import forms  
from release.models import ReleasePost
from django import forms
from django.contrib.contenttypes import fields
from django.forms import widgets
 
class ReleaseForm(forms.ModelForm):  
    class Meta:  
        model = ReleasePost  
        fields = ['title','thumbnail', 'image_url', 'overview',
                'categories'] #https://docs.djangoproject.com/en/3.0/ref/forms/widgets/
        widgets = { 'title': forms.TextInput(attrs={ 'class': 'form-control' }), 
            'categories': forms.TextInput(attrs={ 'class': 'form-control' }),
            'overview': forms.TextInput(attrs={ 'class': 'form-control' }),
            'thumbnail': forms.FileInput(attrs={ 'class': 'form-control' }),
            
      }

