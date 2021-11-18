from django.urls import path
from release import views
from release.views import releaseblog
from django.conf.urls import url
from release.views import  cadastrar_release, editar_release, remover_release, index_release

urlpatterns = [
    #path("", home, name="home"),
    path("novidades/", views.releaseblog, name="releaseblog"),
    url(r'^release_dashboard/editar/(?P<pk>[0-9]+)', editar_release, name='editar_release'),
    url(r'^release_dashboard/remover/(?P<pk>[0-9]+)', remover_release, name='remover_release'),
    url(r'^release_form_dashboard/', cadastrar_release, name='cadastrar_release'),
    url(r'release-dashboard/', index_release, name=('index_release')),
    ]