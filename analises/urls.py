from django.urls import path
from analises import views
from analises.views import releaseblog
from django.conf.urls import url

urlpatterns = [
    #path("", home, name="home"),
    path("relatorios-dashboard/", views.releaseblog, name="relatorios-dashboard"),
    
    ]