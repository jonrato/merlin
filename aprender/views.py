from django.shortcuts import render
from django_app.models import Cursos

def aprender(request):
    template_name="aprender.html"
    context = {}
    cursos = Cursos.objects.all()
    context = {'cursos': cursos}
    return render(request, 'aprender.html', context)

