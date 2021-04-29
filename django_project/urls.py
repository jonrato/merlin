"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import include, path
from machina import urls as machina_urls
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from login import views
from django.contrib import admin




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aprender.urls')),
    path('', include('dashboard.urls')),
    path('forum/', include(machina_urls)),
    path('', include('sobre.urls')),
    path('', include('django_app.urls')),
    path('noticias/', include('blog_noticias.urls')),
    path('', include('blog_noticias.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('django_app.urls')),
    url(r'^',include('login.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

