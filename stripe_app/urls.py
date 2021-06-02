from django.urls import path, include
from stripe_app import views

urlpatterns = [
    path('join', views.join, name='join'),
    path('checkout', views.checkout, name='checkout'),
    path('order/<int:pk>', views.edit_order, name='edit_order'),
    path('auth/settings', views.settings, name='settings'),
]