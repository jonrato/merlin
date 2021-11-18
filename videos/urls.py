from django.urls import path
from django_app import views
from videos.views import  cadastrar_video, editar_video, remover_video, index_video

from django.conf.urls import url

urlpatterns = [
    
    #vídeo
    path('videos-dashboard/', views.index_video, name=('index_video')),
    url(r'^video_dashboard/editar/(?P<pk>[0-9]+)', editar_video, name='editar_video'),
    url(r'^video_dashboard/remover/(?P<pk>[0-9]+)', remover_video, name='remover_video'),
    url(r'^video_form_dashboard/', cadastrar_video, name='cadastrar_video'),
    
    
    ]