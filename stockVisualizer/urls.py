from django.contrib import admin
from django.urls import path
import stockVisualizer.views

urlpatterns = [
    path('stock_data/', stockVisualizer.views.home, name='stock_data'),
    path('get_stock_data/', stockVisualizer.views.get_stock_data),
]