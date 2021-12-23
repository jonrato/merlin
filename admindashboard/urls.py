from admindashboard.models import Dashboard_home, Dashboard_videos
from django.urls import path
from admindashboard import views
from history.views import HistoryList
from django.conf.urls import url

from .views import CampoList, custom_noticias, custom_sobre
urlpatterns = [
    path('custom-home/', views.custom_home, name=('custom_home')),
    
    url(r'^custom-sobre/', custom_sobre, name='custom_sobre'),
    url(r'^custom-noticias/', custom_noticias, name='custom_noticias'),

    url(r'^custom-dashboard-home/', Dashboard_home, name='Dashboard_home'),
    url(r'^custom-dashboard-videos/', Dashboard_videos, name='Dashboard_videos'),

    path('admin-dashboard/', views.admin_dashboard, name=('admin-dashboard')),
    path('analitico-dashboard/', views.analitico_dashboard, name=('analitico-dashboard')),
    path('artigos-dashboard/', views.artigos_dashboard, name=('artigos-dashboard')),
    path('forum-dashboard/', views.forum_dashboard, name=('forum-dashboard')),
    #path('usuarios-dashboard/', views.usuarios_dashboard, name=('usuarios-dashboard')),
    path('usuarios-dashboard/', CampoList.as_view(), name=('campolist-dashboard')),
    path('vendas-dashboard/', views.vendas_dashboard, name=('vendas-dashboard')),

    
    ]