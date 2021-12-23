from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
#página sobre
class Sobre(models.Model):
    image_professional1 = models.ImageField()
    nome_professional1 = models.CharField(max_length=255)
    cargo_professional1 = models.CharField(max_length=255)

    image_professional2 = models.ImageField()
    nome_professional2 = models.CharField(max_length=255)
    cargo_professional2 = models.CharField(max_length=255)

    image_professional3 = models.ImageField()
    nome_professional3 = models.CharField(max_length=255)
    cargo_professional3 = models.CharField(max_length=255)

#end página sobre
