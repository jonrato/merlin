from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models import UpdateHome
from videos.models import Post

#DASHBOARD HOME
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def update(request, update_id):
    update = UpdateHome.objects.get(pk=update_id)
    return render(request, 'dashboard.html', {'update': update})

#END DASHBOARD HOME


@login_required
def assinatura(request):
    return render(request, 'dashboard-assinaturas.html')

@login_required
def especialista(request):
    return render(request, 'dashboard-especialista.html')



@login_required
def perfil(request):
    return render(request, 'dashboard-perfil.html')

@login_required
def videos(request):
    video = Post.objects.all()
    context = {'video': video}
    return render(request, 'dashboard-videos.html', context)
