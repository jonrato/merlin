from django.urls import path
from aprender import views
urlpatterns = [
    
    path('aprender/', views.aprender, name=('aprender')),
    
    ]