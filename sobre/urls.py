from django.urls import path
from sobre import views

urlpatterns = [
    path('sobre/', views.sobre, name=('sobre')),
    
    ]