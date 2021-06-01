
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
from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.shortcuts import reverse
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation

User = get_user_model()

class Author_Assinaturas(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to="")

    def __str__(self):
        return self.user.username

class Category_Assinaturas(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

class Comment_Assinaturas(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    apost = models.ForeignKey('Post_Assinaturas', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.username


class Post_Assinaturas(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    thumbnail = models.ImageField(upload_to="", null=True, blank=True)
    image_url = models.CharField(max_length=500, default=None, null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    content = RichTextField(null=True, blank=True)
    author = models.ForeignKey(Author_Assinaturas, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category_Assinaturas)
    published = models.BooleanField()
    

    @property
    def post_link(self):
        return reverse("apost", kwargs={
            'slug':self.slug
        })
    
    def get_absolute_url(self):
        return reverse('apost', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


#end página assinaturas
    
