from django.urls import path
from django_app import views
from django_app.views import AssinaturasList, APostDetailView,index_curso, cadastrar_curso, editar_curso, remover_curso, cadastrar_assinatura, cadastrar_autor, cadastrar_categoria, editar_assinatura, editar_autor, editar_categoria, index_assinaturas, listar_assinatura, listar_assinaturas_categoria, listar_autor, listar_autor_assinatura, listar_categoria, perfil_autor, remover_assinatura, remover_autor, remover_categoria

from django.conf.urls import url

urlpatterns = [
    path('', views.index, name=('index')),
    
    
    #curso
    path('produtos-dashboard/', views.index_curso, name=('index_curso')),
    url(r'^curso_dashboard/editar/(?P<pk>[0-9]+)', editar_curso, name='editar_curso'),
    url(r'^curso_dashboard/remover/(?P<pk>[0-9]+)', remover_curso, name='remover_curso'),
    url(r'^curso_dashboard/', cadastrar_curso, name='cadastrar_curso'),
    
    
    #assinaturas
    url(r'^assinatura_dashboard/home', index_assinaturas, name='index_assinaturas'),
    url(r'^assinatura_dashboard/cadastrar/', cadastrar_assinatura, name='cadastrar_assinatura'),
    url(r'^assinatura_dashboard/listar/', listar_assinatura, name='listar_assinatura'),
    url(r'^assinatura_dashboard/editar/(?P<pk>[0-9]+)', editar_assinatura, name='editar_assinatura'),
    url(r'^assinatura_dashboard/autor/assinatura/(?P<pk>[0-9]+)', listar_autor_assinatura, name='listar_autor_assinatura'),
    url(r'^assinatura_dashboard/remover/(?P<pk>[0-9]+)', remover_assinatura, name='remover_assinatura'),

    url(r'^author/cadastrar/', cadastrar_autor, name='cadastrar_autor'),
    url(r'^author/listar/', listar_autor, name='listar_autor'),
    url(r'^author/editar/(?P<pk>[0-9]+)', editar_autor, name='editar_autor'),
    url(r'^author/remover/(?P<pk>[0-9]+)', remover_autor, name='remover_autor'),
    url(r'^author/perfil/(?P<pk>[0-9]+)', perfil_autor, name='perfil_autor'),

    url(r'^categoria/cadastrar/', cadastrar_categoria, name='cadastrar_categoria'),
    url(r'^categoria/listar/', listar_categoria, name='listar_categoria'),
    url(r'^categoria/editar/(?P<pk>[0-9]+)', editar_categoria, name='editar_categoria'),
    url(r'^categoria/remover/(?P<pk>[0-9]+)', remover_categoria, name='remover_categoria'),
    url(r'^categoria/produto/(?P<pk>[0-9]+)', listar_assinaturas_categoria, name='listar_assinaturas_categoria'),
    ]