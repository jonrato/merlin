from django.shortcuts import render
from django.http import HttpResponse
from sobre.models import Sobre

def sobre(request):
    
    return render(request, 'sobre.html')

#sobre
def sobre(request):
    sobre = Sobre.objects.get
    return render(request, 'sobre.html', {'sobre': sobre})
#end sobre