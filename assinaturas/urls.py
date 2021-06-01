from django.urls import path
from assinaturas import views


urlpatterns = [
    
    path('assinaturas-acoes/', views.assinaturas_acoes, name=('assinaturas-acoes')),
    path('assinaturas-completo/', views.assinaturas_completo, name=('assinaturas-completo')),
    path('assinaturas-dividendos/', views.assinaturas_dividendos, name=('assinaturas-dividendos')),
    path('assinaturas-fiis/', views.assinaturas_fiis, name=('assinaturas-fiis')),
    path('assinaturas-small-caps/', views.assinaturas_small_caps, name=('assinaturas-small-caps')),
    path('assinaturas-trader/', views.assinaturas_trader, name=('assinaturas-trader')),
    ]