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
from hitcount.views import HitCountDetailView
from django.views.generic.detail import DetailView

#Listar todos os Posts
from django.core import paginator
from django.db.models import query
from django.shortcuts import render, redirect, reverse
from django.views.generic.detail import DetailView
from blog_noticias.models import Category, Comment, Post
from hitcount.views import HitCountDetailView
from blog_noticias.forms import CommentForm
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
from django.db.models import Q
from hitcount.models import HitCount

#End Listar todos os Posts

#Assinaturas e Cursos
from .models import Assinaturas, Cursos
#from .models import home_view  assinaturas_view, aprender_view, sobre_view, noticias_view, login_view
#End Assinaturas e Cursos

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
    

    context = {}
    posts = Post.objects.all()
    categories = Category.objects.all()
    popular_posts = Post.objects.order_by('-hit_count_generic')[:4]

    page = request.GET.get("page")
    paginator = Paginator(posts, 4)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'popular_posts':popular_posts,
        'categories':categories,
        'posts': posts,
    }

    
#End Listar todos os Posts
    return render(request, 'dashboard-admin/artigos.html', context)

@login_required
def forum_dashboard(request):
    return render(request, 'dashboard-admin/forum.html')

@login_required
def produtos_dashboard(request):
    assinaturas = Assinaturas.objects.all()
    cursos = Cursos.objects.all()
    context = {
        'assinaturas': assinaturas,
        'cursos': cursos,
    }


    return render(request, 'dashboard-admin/produtos.html', context)


    
            



@login_required
def usuarios_dashboard(request):
    return render(request, 'dashboard-admin/usuarios.html')

@login_required
def vendas_dashboard(request):
    return render(request, 'dashboard-admin/vendas.html')