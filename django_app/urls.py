from django.urls import path
from django_app import views
from django_app.views import AssinaturasList, APostDetailView

from django.conf.urls import url

urlpatterns = [
    path('', views.index, name=('index')),
    
    
    path('assinaturas/', views.Assinaturas, name=('assinaturas')),
    path("assinaturas/", AssinaturasList.as_view(), name="assinaturas"),
    path("assinaturas/<slug>", APostDetailView.as_view(), name="apost"),
    path('admin-dashboard/', views.index_admin, name=('index_admin')),

    url(r'produtos-dashboard/create$', views.create_curso, name='create'),
    url(r'produtos-dashboard/edit_curso/(?P<id>\d+)$', views.edit_curso, name='edit'),
    url(r'produtos-dashboard/edit_curso/update_curso/(?P<id>\d+)$', views.update_curso, name='update'),
    url(r'produtos-dashboard/(?P<id>\d+)$', views.update_curso, name='delete'),
    
    ]