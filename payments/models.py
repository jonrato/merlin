from django.db import models
from django.core import validators
from django.db.models.deletion import PROTECT

class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=70, verbose_name='Nome do Produto')
    description = models.TextField(max_length=800, verbose_name='Descrição')
    price = models.TextField(verbose_name='Preço', )
    
class OrderDetail(models.Model):

    id = models.BigAutoField(primary_key=True)
    costumer_email = models.EmailField(verbose_name='Customer Email') #devo ter retirado esse trecho do template html
    product = models.ForeignKey(
        to=Product,
        verbose_name='Produto',
        on_delete=models.PROTECT
    )

    # You can change as a Foreign Key to the user model
    customer_email = models.EmailField(
        verbose_name='Customer Email', blank=True
    )

    amount = models.IntegerField(
        verbose_name='quantidade'
    )
    stripe_payment_intent = models.CharField(max_length=200)

    #This field can be changed as status
    has_paid = models.BooleanField(default=False, verbose_name='Status de Pagamento')
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)