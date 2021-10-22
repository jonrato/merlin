from django.shortcuts import render
import json
from .models import ProductChart

def products(request):
    queryset = ProductChart.objects.all()
    months = [obj.month for obj in queryset]
    prices = [int(obj.price) for obj in queryset]

    context = {
        'months': json.dumps(months),
        'prices': json.dumps(prices),
    }
    return render(request, 'charts/products.html', context)
