from django.shortcuts import render
from django.http import HttpResponse
from django_app.models import Home, Assinaturas
from admindashboard.models import PostHome

#home
def index(request):

    context = {}
    posts = PostHome.objects.all()
    
    context = {
        
        'posts': posts,
    }
    return render(request, 'home.html', context)

def home(request, home_id):
    home = Home.objects.get(pk=home_id)
    return render(request, 'home.html', {'home': home})
#end home

#assinaturas
def assinaturas(request):
    return render(request, 'assinaturas.html')


def assinaturas(request):
    assinaturas = Assinaturas.objects.all()
    return render(request, 'assinaturas.html', {'assinaturas': assinaturas})

#end assinaturas

