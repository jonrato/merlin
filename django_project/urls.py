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

from django.contrib import admin
from common.views import SignUpView, ProfileUpdateView, ProfileView
from django.contrib.auth import views as auth_views

app_name = 'aprender'



urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('charts.urls')),
    path('history/', include('history.urls')),
    path('', include('stripe_app.urls')),
    path('cart/', include('cart.urls')),
    path('', include('admindashboard.urls')),
    path('', include('especialista.urls')),
    path('', include('assinaturas.urls')),
    path('', include('aprender.urls')),
    path('', include('dashboard.urls')),
    path('forum/', include(machina_urls)),
    path('', include('sobre.urls')),
    path('', include('django_app.urls')),
    path('', include('blog_noticias.urls')),
    path('', include('release.urls')),
    path('', include('analises.urls')),
    path('', include('stockVisualizer.urls')),
    #path('', include('blog_noticias.urls'), name="noticias"),
    path('register/', SignUpView.as_view(), name="register"),
    path('login/', auth_views.LoginView.as_view(
        template_name='login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='login'
    ), 
    name='logout'),
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='change-password.html',
            success_url='/'
        ),
        name='change-password'
    ),
    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),

    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password-reset/password_reset.html',
             subject_template_name='common/password-reset/password_reset_subject.txt',
             email_template_name='common/password-reset/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    #End Forget Password
    path('', include('blog_noticias.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('django_app.urls')),
    path('', include('payments.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)