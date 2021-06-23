from django.urls import path
from blog_noticias import views
from blog_noticias.views import PostDetailView ,cadastrar_noticia, editar_noticia, listar_comentario, listar_comentario_noticia, remover_comentario ,remover_noticia, searchBlog, PostList
from django.conf.urls import url

urlpatterns = [
    #path("", home, name="home"),
    path("noticias/", views.blog, name="blog"),
    path("noticias/", PostList.as_view(), name="blog"),
    #path('admin-dashboard', PostList.as_view(), name='admin-dashboard'),
    path("noticias/<slug>", PostDetailView.as_view(), name="post"),
    path("admin-dashboard/", views.boracontar, name="boracontar"),
    path("q/", searchBlog, name="search"),


    url(r'^noticia_dashboard/cadastrar/', cadastrar_noticia, name='cadastrar_noticia'),
    url(r'^noticia_dashboard/editar/(?P<pk>[0-9]+)', editar_noticia, name='editar_noticia'),
    url(r'^noticia_dashboard/remover/(?P<pk>[0-9]+)', remover_noticia, name='remover_noticia'),

    url(r'^comentario/listar/', listar_comentario, name='listar_comentario'),
    url(r'^comentario/remover/(?P<pk>[0-9]+)', remover_comentario, name='remover_comentario'),
    url(r'^comentario/noticia/(?P<pk>[0-9]+)', listar_comentario_noticia, name='listar_comentario_noticia'),
    ]