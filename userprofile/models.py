from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=12, blank=True)
    cidade = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=5, blank=True)
    profile_image = models.ImageField(upload_to='users/', null=True, blank=True, default='user.png')

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

@property
def image_url(self):
    if self.profile_image and hasattr(self.profile_image, 'url'):
        return self.image_url

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
