from django.urls import path
from blog_noticias import views
from blog_noticias.views import blog, PostDetailView, searchBlog, PostList
urlpatterns = [
    #path("", home, name="home"),
    path("noticias/", views.blog, name="blog"),
    path("noticias/", PostList.as_view(), name="blog"),
    #path('admin-dashboard', PostList.as_view(), name='admin-dashboard'),
    path("noticias/<slug>", PostDetailView.as_view(), name="post"),
    path("q/", searchBlog, name="search"),
    ]