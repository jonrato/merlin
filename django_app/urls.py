from django.urls import path
from django_app import views
from django_app.views import AssinaturasList, APostDetailView

urlpatterns = [
    path('', views.index, name=('index')),
    path('assinaturas/', views.Assinaturas, name=('assinaturas')),
    path("assinaturas/", AssinaturasList.as_view(), name="assinaturas"),
    path("assinaturas/<slug>", APostDetailView.as_view(), name="apost"),
    path('admin-dashboard/', views.index_admin, name=('index_admin')),
    
    ]