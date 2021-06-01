from django.urls import path
from admindashboard import views
from history.views import HistoryList

from .views import CampoList
urlpatterns = [
    path('admin-dashboard/', views.admin_dashboard, name=('admin-dashboard')),
    
    path('analitico-dashboard/', views.analitico_dashboard, name=('analitico-dashboard')),
    path('artigos-dashboard/', views.artigos_dashboard, name=('artigos-dashboard')),
    path('forum-dashboard/', views.forum_dashboard, name=('forum-dashboard')),
    path('produtos-dashboard/', views.produtos_dashboard, name=('produtos-dashboard')),
    #path('usuarios-dashboard/', views.usuarios_dashboard, name=('usuarios-dashboard')),
    path('usuarios-dashboard/', CampoList.as_view(), name=('campolist-dashboard')),
    path('vendas-dashboard/', views.vendas_dashboard, name=('vendas-dashboard')),

    
    ]