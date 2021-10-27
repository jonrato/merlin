from django import forms
from core.models import FileHandler

class FileHandlerForm(forms.ModelForm):
    file_uploaded = forms.FileField()

    class Meta():
        model = FileHandler
        fields = ("file_upload","criado","name","resume")