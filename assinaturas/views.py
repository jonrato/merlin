
from django_app.models import Category_Assinaturas
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic import ListView, DetailView
from django_app.models import Post_Assinaturas, Category_Assinaturas




def assinaturas_acoes(request):
    return render(request, 'assinaturas/acoes.html')

def assinaturas_completo(request):
    return render(request, 'assinaturas/completo.html')

def assinaturas_dividendos(request):
    return render(request, 'assinaturas/dividendos.html')

def assinaturas_fiis(request):
    return render(request, 'assinaturas/fiis.html')

def assinaturas_small_caps(request):
    return render(request, 'assinaturas/small-caps.html')

def assinaturas_trader(request):
    return render(request, 'assinaturas/trader.html')