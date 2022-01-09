
from django.db import models
from django.core import validators
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    

    id = models.BigAutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=70,
        verbose_name='Product Name'
    )

    description = models.TextField(
        max_length=800,
        verbose_name='Description'
    )

    price = models.FloatField(
        verbose_name='Price',
        validators=[
            validators.MinValueValidator(1),
            validators.MaxValueValidator(100000)
        ]
    )
    Image_pic = models.ImageField(upload_to="upload/", blank="True", null="True")

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)

class OrderDetail(models.Model):

    user = models.OneToOneField(
        User,on_delete=models.CASCADE, blank=True, null=True
        )

    id = models.BigAutoField(
        primary_key=True
    )

    # You can change as a Foreign Key to the user model
    customer_email = models.EmailField(
        verbose_name='Customer Email'
    )

    product = models.ForeignKey(
        to=Product,
        verbose_name='Product',
        on_delete=models.PROTECT
    )

    amount = models.IntegerField(
        verbose_name='Amount'
    )

    stripe_payment_intent = models.CharField(
        max_length=200
    )

    # This field can be changed as status
    has_paid = models.BooleanField(
        default=False,
        verbose_name='Payment Status'
    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    updated_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return '%s %s' % (self.user.first_name, self.user.last_name)