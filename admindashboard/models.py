from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from hitcount.models import HitCount
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField





User = get_user_model()


class Alguem(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="")

    def __str__(self):
        return self.user.username
#Model da Página Inicial
class PostHome(models.Model):
    text_nosso_time = models.TextField(null=True, blank=True)
    thumbnailA = models.ImageField(upload_to="", null=True, blank=True)
    thumbnailB = models.ImageField(upload_to="", null=True, blank=True)
    thumbnailC = models.ImageField(upload_to="", null=True, blank=True)
    nameA = models.TextField()
    nameB = models.TextField()
    nameC = models.TextField()
    paragraphy1 = models.TextField(null=True, blank=True)
    paragraphyImage1 = models.ImageField(upload_to="", null=True, blank=True)
    paragraphy2 = models.TextField(null=True, blank=True)
    paragraphyImage2 = models.ImageField(upload_to="", null=True, blank=True)
    comentario = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(null=True)
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
    text_capa = models.TextField(null=True, blank=True)
    DescrilcaoMerlin = models.TextField(null=True, blank=True)
    thumbnailQuemSomos = models.ImageField(upload_to="", null=True, blank=True)
    DescricaoQuemSomos = models.TextField(null=True, blank=True)
    thumbnaiImageA = models.ImageField(upload_to="", null=True, blank=True)
    text_titleA = models.TextField(null=True, blank=True)
    thumbnaiImageB = models.ImageField(upload_to="", null=True, blank=True)
    text_titleB = models.TextField(null=True, blank=True)
    thumbnaiImageC = models.ImageField(upload_to="", null=True, blank=True)
    text_titleC = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(null=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    @property
    def post_link(self):
        return reverse("post", kwargs={
            
        })

    def __str__(self):
        return self.text_capa
    #END Model Quem Somos


    #Model Página Notícias
class PostNoticias(models.Model):
    thumbnailCarrossel1 = models.ImageField(upload_to="", null=True, blank=True)
    title1 = models.TextField()
    text1 = models.TextField(null=True, blank=True)
    thumbnailCarrossel2 = models.ImageField(upload_to="", null=True, blank=True)
    title2 = models.TextField()
    text2 = models.TextField(null=True, blank=True)
    thumbnailCarrossel3 = models.ImageField(upload_to="", null=True, blank=True)
    title3 = models.TextField()
    text3 = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(null=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    @property
    def post_link(self):
        return reverse("post", kwargs={
            
        })

    #def __str__(self):
    #    return self.thumbnailCarrossel1
    #END Model Página Notícias


#Model Dashboard home, análises, vídeos
class Dashboard_home(models.Model):
    image_header = models.ImageField(upload_to="", null=True, blank=True)
    text_header = models.TextField()
    link_header = models.TextField()
    noticias_hoje = models.ImageField(upload_to="", null=True, blank=True)
    link_noticias_hoje = models.TextField()
    bolsa_hoje = models.ImageField(upload_to="", null=True, blank=True)
    link_bolsa_hoje = models.TextField()
    published = models.BooleanField(null=True)

#class dashboard_analises(models.Model):

class Dashboard_videos(models.Model):
    image_capa = models.ImageField(upload_to="", null=True, blank=True)
    titulo_capa = models.TextField()
    text_capa = models.TextField()
    link_capa = models.TextField()
    published = models.BooleanField(null=True)
#END Model Dashboard home, análises, vídeos



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