from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount
from django.shortcuts import reverse
from django.contrib.auth import get_user_model


User = get_user_model()

class Alguem(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="")

    def __str__(self):
        return self.user.username
#Model da Página Inicial
class PostHome(models.Model):
    text_nosso_time = models.TextField()
    thumbnailA = models.ImageField(upload_to="", null=True, blank=True)
    thumbnailB = models.ImageField(upload_to="", null=True, blank=True)
    thumbnailC = models.ImageField(upload_to="", null=True, blank=True)
    nameA = models.TextField()
    nameB = models.TextField()
    nameC = models.TextField()
    paragraphy1 = models.TextField()
    paragraphyImage1 = models.ImageField(upload_to="", null=True, blank=True)
    paragraphy2 = models.TextField()
    paragraphyImage2 = models.ImageField(upload_to="", null=True, blank=True)
    comentario = models.TextField()
    date = models.DateTimeField(auto_now=True)
    published = models.BooleanField()
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    @property
    def post_link(self):
        return reverse("post", kwargs={
            
        })

    def __str__(self):
        return self.text_nosso_time
    #END Model da Página Inicial

    #Model QuemSomos
class PostQuemSomos(models.Model):
    thumbnailCapa = models.ImageField(upload_to="", null=True, blank=True)
    text_capa = models.TextField()
    DescrilcaoMerlin = models.TextField()
    thumbnailQuemSomos = models.ImageField(upload_to="", null=True, blank=True)
    DescricaoQuemSomos = models.TextField()
    thumbnaiImageA = models.ImageField(upload_to="", null=True, blank=True)
    text_titleA = models.TextField()
    thumbnaiImageB = models.ImageField(upload_to="", null=True, blank=True)
    text_titleB = models.TextField()
    thumbnaiImageC = models.ImageField(upload_to="", null=True, blank=True)
    text_titleC = models.TextField()
    date = models.DateTimeField(auto_now=True)
    published = models.BooleanField()
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    @property
    def post_link(self):
        return reverse("post", kwargs={
            
        })

    def __str__(self):
        return self.text_capa
    #END Model Quem Somos




class Users(models.Model):
    user=models.TextField(default=None)
    def __str__(self):
        return self.user

class Assinaturas(models.Model):
    name = models.TextField()
    price = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image_url = models.CharField(max_length=500, default=None, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['created']


class Cursos(models.Model):
    name = models.TextField()
    price = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    image_url = models.CharField(max_length=500, default=None, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['created']