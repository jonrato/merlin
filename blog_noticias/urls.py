from django.urls import path
from blog_noticias.views import blog, PostDetailView, searchBlog
urlpatterns = [
    #path("", home, name="home"),
    path("noticias/", blog, name="blog"),
    path("noticias/<slug>", PostDetailView.as_view(), name="post"),
    path("q/", searchBlog, name="search"),
    ]