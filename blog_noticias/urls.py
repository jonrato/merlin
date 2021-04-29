from django.urls import path
from blog_noticias import views
urlpatterns = [
    path('', views.blog, name=('blog')),
    path('posts/<int:post_id>', views.post, name=('post'))
    ]