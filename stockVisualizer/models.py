from django.db import models
from django.db.models.base import Model

class StockData(models.Model):
    symbol = models.TextField(null=True)
    data = models.TextField(null=True)