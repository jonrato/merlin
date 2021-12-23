from django.db import models

from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class UpdateHome(models.Model):
    Image = models.ImageField()
    Noticias_summary = models.CharField(max_length=255)
    Noticias_image = models.ImageField()
    Cursos_summary = models.CharField(max_length=255)
    Cursos_image = models.ImageField()
    Bolsa_summary = models.CharField(max_length=255)
    Bolsa_image = models.ImageField()
    Video_summary = models.CharField(max_length=255)
    Video_image = models.ImageField()


    def __str__(self):
        return self.Image
