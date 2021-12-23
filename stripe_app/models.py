from django.db import models
from django.contrib.auth.models import User

class Size(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Icecream(models.Model):
    topping1 = models.CharField(max_length=100)
    topping2 = models.CharField(max_length=100)

    size = models.ForeignKey(Size, on_delete=models.CASCADE)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    stripeid = models.CharField(max_length=255)
    stripe_subscription_id = models.CharField(max_length=255)
    cancel_at_period_end = models.BooleanField(default=False)
    
