from django.db import models
from cart.models import Cart

ORDER_STATUS_CHOICES = (
    ('created', 'Criado'),
    ('paid', 'Pago'),
    ('shiped', 'Enviado'),
    ('refunded', 'Devolvido'),
)

class Order(models.Model):
    order_id = models.CharField(max_length=120, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, null=True)
    status = models.CharField(max_length=120, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def __str__(self):
        return self.order_id

