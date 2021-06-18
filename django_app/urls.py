from django.urls import path
from django_app import views
from django_app.views import AssinaturasList, APostDetailView, cadastrar_assinatura, cadastrar_autor, cadastrar_categoria, editar_assinatura, editar_autor, editar_categoria, listar_assinatura, listar_assinaturas_categoria, listar_autor, listar_autor_assinatura, listar_categoria, perfil_autor, remover_assinatura, remover_autor, remover_categoria

from django.conf.urls import url

urlpatterns = [
    path('', views.index, name=('index')),
    
    
    path('assinaturas/', views.Assinaturas, name=('assinaturas')),
    path("assinaturas/", AssinaturasList.as_view(), name="assinaturas"),
    path("assinaturas/<slug>", APostDetailView.as_view(), name="apost"),
    path('admin-dashboard/', views.index_admin, name=('index_admin')),
    
    url(r'produtos-dashboard/create_assinatura$', views.create_assinaturas, name='create_assinatura'),
    url(r'produtos-dashboard/create$', views.create_curso, name='create'),
    url(r'produtos-dashboard/edit_cursos/(?P<id>\d+)$', views.edit_curso, name='edit_cursos'),
    url(r'produtos-dashboard/edit_curso/update_curso/(?P<id>\d+)$', views.update_curso, name='update'),
    url(r'produtos-dashboard/(?P<id>\d+)$', views.update_curso, name='delete'),
    
    #assinaturas
    url(r'^assinatura_dashboard/cadastrar/', cadastrar_assinatura, name='cadastrar_assinatura'),
    url(r'^assinatura_dashboard/listar/', listar_assinatura, name='listar_assinatura'),
    url(r'^assinatura_dashboard/editar/(?P<pk>[0-9]+)', editar_assinatura, name='editar_assinatura'),
    url(r'^assinatura_dashboard/produto/(?P<pk>[0-9]+)', listar_autor_assinatura, name='listar_autor_assinatura'),
    url(r'^assinatura_dashboard/remover/(?P<pk>[0-9]+)', remover_assinatura, name='remover_assinatura'),

    url(r'^author/cadastrar/', cadastrar_autor, name='cadastrar_autor'),
    url(r'^author/listar/', listar_autor, name='listar_autor'),
    url(r'^author/editar/(?P<pk>[0-9]+)', editar_autor, name='editar_autor'),
    url(r'^author/remover/(?P<pk>[0-9]+)', remover_autor, name='remover_remover_autor'),
    url(r'^author/perfil/(?P<pk>[0-9]+)', perfil_autor, name='perfil_autor'),

    url(r'^categoria/cadastrar/', cadastrar_categoria, name='cadastrar_categoria'),
    url(r'^categoria/listar/', listar_categoria, name='listar_categoria'),
    url(r'^categoria/editar/(?P<pk>[0-9]+)', editar_categoria, name='editar_categoria'),
    url(r'^categoria/remover/(?P<pk>[0-9]+)', remover_categoria, name='remover_categoria'),
    url(r'^categoria/produto/(?P<pk>[0-9]+)', listar_assinaturas_categoria, name='listar_assinaturas_categoria'),
    ]