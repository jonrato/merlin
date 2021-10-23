from django.urls import path
from release import views
from release.views import releaseblog
from django.conf.urls import url

urlpatterns = [
    #path("", home, name="home"),
    path("novidades/", views.releaseblog, name="releaseblog"),
    
    ]