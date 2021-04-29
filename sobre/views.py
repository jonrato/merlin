from django.shortcuts import render
from django.http import HttpResponse
from sobre.models import Sobre

def sobre(request):
    
    return render(request, 'sobre.html')

#sobre
def sobre(request, sobre_id):
    sobre = Sobre.objects.get(pk=sobre_id)
    return render(request, 'sobre.html', {'sobre': sobre})
#end sobre