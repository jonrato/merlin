from cart.views import cart_home, cart_update,checkout_home
from django.urls import include, path

app_name = "cart"

from .views import (
    cart_home,
    checkout_home,
    cart_update,
)

urlpatterns = [
    path('', cart_home,name='home'),
    path('checkout/', checkout_home, name='checkout'),
    path('update/', cart_update, name='update')
]