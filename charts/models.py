from __future__ import unicode_literals
from django.db import models


class ProductChart(models.Model):
    month = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return self.month