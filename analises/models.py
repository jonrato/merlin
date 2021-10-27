from django.db import models
from ckeditor.fields import RichTextField
import os

def file_path(instance, filename):
    path="documents/"
    format = 'uploaded-' + filename
    return os.path.join(path, format)

class FileHandler(models.Model):

    file_upload = models.FileField(upload_to=file_path)
    criado = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação", blank=True, null=True)
    name = models.CharField(max_length=50)
    resume = RichTextField(null=True, blank=True)
    
    def __str__(self):
        return str(self.file_upload)