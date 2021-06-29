from django.urls import path
from especialista import views
from especialista.views import DetailView , PList
from django.conf.urls import url


urlpatterns = [
    path("chat/", views.Chatblog, name="chat_blog"),
    path("chat/", PList.as_view(), name="chat_blog"),
    path("chat/<slug>", DetailView.as_view(), name="chat_post"),
]