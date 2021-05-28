from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models import UpdateHome
from blog_noticias.models import Post

#DASHBOARD HOME
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def update(request, update_id):
    update = UpdateHome.objects.get(pk=update_id)
    return render(request, 'dashboard.html', {'update': update})

#END DASHBOARD HOME
@login_required
def analise(request):
    return render(request, 'dashboard-analises.html')

@login_required
def assinatura(request):
    return render(request, 'dashboard-assinaturas.html')

@login_required
def especialista(request):
    return render(request, 'dashboard-especialista.html')

#dashboard noticias
@login_required
def noticia(request):
    return render(request, 'dashboard-noticias.html')

#end dashboard noticias

@login_required
def perfil(request):
    return render(request, 'dashboard-perfil.html')

@login_required
def videos(request):
    return render(request, 'dashboard-videos.html')