from django.conf.urls import url
from django.contrib import admin
from charts import views

urlpatterns = [
    url(r'^chart-month/$', views.products, name='chart-month'),
]