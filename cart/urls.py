from cart.views import cart_home, cart_update
from django.urls import include, path

app_name = "cart"

from .views import (
    cart_home,
    cart_update,
)

urlpatterns = [
    path('', cart_home,name='home'),
    path('update/', cart_update, name='update')
]