from django.contrib.auth.models import User
from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Postpost(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
    summary = RichTextField()
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Category)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title