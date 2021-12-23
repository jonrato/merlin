from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    link = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="upload/", null=True, blank=True)

    def __str__(self):
        return self.title