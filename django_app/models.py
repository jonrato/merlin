
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

#página home
class Home(models.Model):
    image_professional1 = models.ImageField()
    nome_professional1 = models.CharField(max_length=255)
    cargo_professional1 = models.CharField(max_length=255)

    image_professional2 = models.ImageField()
    nome_professional2 = models.CharField(max_length=255)
    cargo_professional2 = models.CharField(max_length=255)

    image_professional3 = models.ImageField()
    nome_professional3 = models.CharField(max_length=255)
    cargo_professional3 = models.CharField(max_length=255)

#end página home

#página assinaturas
class Assinaturas(models.Model):
    imagem_curso = models.ImageField()
    titulo_curso = models.CharField(max_length=255)
    professor_curso = models.CharField(max_length=255)
    preco_curso = models.CharField(max_length=255)
    parcela_curso = models.CharField(max_length=255)
    imagem_ebook = models.ImageField()

#end página assinaturas
    
