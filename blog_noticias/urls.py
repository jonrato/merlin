from django.urls import path
from blog_noticias import views
from blog_noticias.views import PostDetailView ,cadastrar_noticia,cadastrar_noticia_categoria,editar_noticia_categoria,remover_noticia_categoria, editar_noticia, listar_comentario, listar_noticia_categoria, remover_comentario ,remover_noticia, searchBlog, PostList
from django.conf.urls import url

urlpatterns = [
    #path("", home, name="home"),
    path("noticias/", views.blog, name="blog"),
    path("noticias/", PostList.as_view(), name="blog"),
    #path('admin-dashboard', PostList.as_view(), name='admin-dashboard'),
    path("noticias/<slug>", PostDetailView.as_view(), name="post"),
    path("admin-dashboard/", views.boracontar, name="boracontar"),
    path("q/", searchBlog, name="search"),

    #noticia
    url(r'^noticia_dashboard/cadastrar/', cadastrar_noticia, name='cadastrar_noticia'),
    url(r'^noticia_dashboard/editar/(?P<pk>[0-9]+)', editar_noticia, name='editar_noticia'),
    url(r'^noticia_dashboard/remover/(?P<pk>[0-9]+)', remover_noticia, name='remover_noticia'),
    #noticia -> comentario
    url(r'^comentario/listar/', listar_comentario, name='listar_comentario'),
    url(r'^comentario/remover/(?P<pk>[0-9]+)', remover_comentario, name='remover_comentario'),
    
    #noticia -> categoria
    url(r'^noticia_dashboard/categoria/cadastrar/',cadastrar_noticia_categoria , name='cadastrar_noticia_categoria'),
    url(r'^noticia_dashboard/categoria/listar', listar_noticia_categoria, name='listar_noticia_categoria'),
    url(r'^noticia_dashboard/categoria/editar/(?P<pk>[0-9]+)',editar_noticia_categoria , name='editar_noticia_categoria'),
    url(r'^noticia_dashboard/categoria/remover/(?P<pk>[0-9]+)', remover_noticia_categoria, name='remover_noticia_categoria'),

    ]