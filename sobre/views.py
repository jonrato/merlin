from django.shortcuts import render
from django.http import HttpResponse
from sobre.models import Sobre
from admindashboard.models import PostQuemSomos

def sobre(request):
    
    return render(request, 'sobre.html')

#sobre
def sobre(request):
    context = {}
    posts = PostQuemSomos.objects.all()
    
    context = {
        
        'posts': posts,
    }
    return render(request, 'sobre.html', context)
    
#end sobre