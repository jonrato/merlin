from django.urls import path
from dashboard import views
urlpatterns = [
    path('dashboard/', views.dashboard, name=('dashboard')),
    path('dashboard-analises/', views.analise, name=('dashboard-analises')),
    path('dashboard-assinaturas/', views.assinatura, name=('dashboard-assinaturas')),
    path('dashboard-especialista/', views.especialista, name=('dashboard-especialista')),
    path('dashboard-noticias/', views.noticia, name=('dashboard-noticias')),
    path('dashboard-perfil/', views.perfil, name=('dashboard-perfil')),
    path('dashboard-videos/', views.videos, name=('dashboard-videos')),

    
    ]