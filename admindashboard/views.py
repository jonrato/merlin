from common.views import ProfileView
from typing import List
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from userprofile.models import Profile
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from .models import Users

#Listar Usuários Cadastrados
class CampoList(ListView):
    model = Profile
    template = "dashboard-admin/usuarios.html"
#End Listar Usuários Cadastrados




#DASHBOARD HOME
@login_required
def admin_dashboard(request):
    usuarios_contagem = User.objects.all().count()
    

    #Pages Views
    
    usuario = Users.objects.all()

    paginator = Paginator(usuario,4)
    page = request.GET.get('page')
    print(page)

    #For IP Adress
    def get_ip(request):
        adress = request.META.get('HTTP_X_FORWARDED_FOR')
        if adress:
            ip = adress.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    ip = get_ip(request)
    u = Users(user=ip)
    print(ip)
    result = Users.objects.filter(Q(user__icontains=ip))
    if len(result) == 1:
        print("user exist")
    elif len(result)>1:
        print("user exist more...")
    else:
        u.save()
        print("user is unique")
    count = Users.objects.all().count()
    print("Total user is", count)

    try:
        usuario=paginator.page(page)
    except PageNotAnInteger:
        usuario=paginator.page(1)
    except EmptyPage:
        usuario=paginator.page(paginator.num_pages)


    

    #End Pages Views
    context = {
        'usuario':usuario,'page':page,'count':count,
        'usuarios_contagem': usuarios_contagem,
    }
    return render(request, 'dashboard-admin/index.html',context)

@login_required
def analitico_dashboard(request):
    return render(request, 'dashboard-admin/analitico.html')

@login_required
def artigos_dashboard(request):
    return render(request, 'dashboard-admin/artigos.html')

@login_required
def forum_dashboard(request):
    return render(request, 'dashboard-admin/forum.html')

@login_required
def produtos_dashboard(request):
    return render(request, 'dashboard-admin/produtos.html')

@login_required
def usuarios_dashboard(request):
    return render(request, 'dashboard-admin/usuarios.html')

@login_required
def vendas_dashboard(request):
    return render(request, 'dashboard-admin/vendas.html')