from django.db import models

from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField
from django.shortcuts import reverse
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation

User = get_user_model()


class ReleaseCategory(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"



class ReleasePost(models.Model):
    title = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='title')
    thumbnail = models.ImageField(upload_to="upload/", null=True, blank=True)
    image_url = models.CharField(max_length=500, default=None, null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(ReleaseCategory)
    published = models.BooleanField()
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk', related_query_name='hit_count_generic_relation')

    @property
    def post_link(self):
        return reverse("post", kwargs={
            'slug':self.slug
        })
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title