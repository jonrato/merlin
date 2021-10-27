from django.urls import path
from analises import views
from analises.views import upload, upload_list, upload_book
from django.conf.urls import url

urlpatterns = [
    #path("", home, name="home"),
    path("relatorios-dashboard/", views.upload,  name="relatorios-dashboard"),
    path('dashboard-analises/', views.upload_list, name=('dashboard-analises')),
    path('dashboard-analises/upload', views.upload_book, name=('dashboard-analises')),
    ]