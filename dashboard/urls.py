from django.urls import path
from dashboard import views
urlpatterns = [
    path('dashboard/', views.dashboard, name=('dashboard')),
    path('dashboard-assinaturas/', views.assinatura, name=('dashboard-assinaturas')),
    path('dashboard-especialista/', views.especialista, name=('dashboard-especialista')),
    path('dashboard-perfil/', views.perfil, name=('dashboard-perfil')),
    path('dashboard-videos/', views.videos, name=('dashboard-videos')),
    

    
    ]