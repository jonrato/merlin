from django.urls import path
from admindashboard import views
from history.views import HistoryList

from .views import CampoList
urlpatterns = [
    path('custom-home/', views.custom_home, name=('custom_home')),
    path('custom-assinaturas/', views.custom_assinaturas, name=('custom_assinaturas')),
    path('custom-aprender/', views.custom_aprender, name=('custom_aprender')),
    path('custom-sobre/', views.custom_sobre, name=('custom_sobre')),
    path('custom-noticias/', views.custom_noticias, name=('custom_noticias')),

    path('admin-dashboard/', views.admin_dashboard, name=('admin-dashboard')),
    path('analitico-dashboard/', views.analitico_dashboard, name=('analitico-dashboard')),
    path('artigos-dashboard/', views.artigos_dashboard, name=('artigos-dashboard')),
    path('forum-dashboard/', views.forum_dashboard, name=('forum-dashboard')),
    path('produtos-dashboard/', views.produtos_dashboard, name=('produtos-dashboard')),
    #path('usuarios-dashboard/', views.usuarios_dashboard, name=('usuarios-dashboard')),
    path('usuarios-dashboard/', CampoList.as_view(), name=('campolist-dashboard')),
    path('vendas-dashboard/', views.vendas_dashboard, name=('vendas-dashboard')),

    
    ]