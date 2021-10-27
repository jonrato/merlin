from django.db import models

class FileUpload(models.Model):
    name = models.CharField(max_length=50)
    resume = models.CharField(max_length=50)
    pdf = models.FileField(upload_to='pdf/')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
