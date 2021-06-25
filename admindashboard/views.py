from admindashboard.models import PostHome, PostQuemSomos, PostNoticias, Dashboard_home, Dashboard_videos
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
from .models import PostHome, Users
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

from django_app.models import Cursos, Post_Assinaturas

@login_required
def produtos_dashboard(request):
    
    template_name="dashboard-admin/produtos.html"
    context = {}
    cursos = Cursos.objects.all()
    assinatura = Post_Assinaturas.objects.all()
    context = {
        'cursos': cursos,
        'assinatura': assinatura

    }
    

    return render(request, 'dashboard-admin/produtos.html', context)


    
            



@login_required
def usuarios_dashboard(request):
    return render(request, 'dashboard-admin/usuarios.html')

@login_required
def vendas_dashboard(request):
    return render(request, 'dashboard-admin/vendas.html')


#CUSTOM PAGES HOME, ASSINATURAS, APRENDER, SOBRE, NOTÍCIAS
from django.shortcuts import get_object_or_404
from django.forms.models import ModelForm

class HomeForm(ModelForm):
    class Meta:
        model = PostHome
        fields = ['text_nosso_time','thumbnailA','thumbnailB','thumbnailC',
                    'nameA','nameB','nameC','paragraphy1','paragraphyImage1',
                    'paragraphy2','paragraphyImage2','comentario','published']


class SobreForm(ModelForm):
    class Meta:
        model = PostQuemSomos
        fields = ['thumbnailCapa','text_capa','DescrilcaoMerlin','thumbnailQuemSomos',
                    'DescricaoQuemSomos','thumbnaiImageA','text_titleA','thumbnaiImageB',
                    'text_titleB','thumbnaiImageC','text_titleC','published']

class NoticiasForm(ModelForm):
    class Meta:
        model = PostNoticias
        fields = ['thumbnailCarrossel1','title1','text1',
        'thumbnailCarrossel2','title2','text2',
        'thumbnailCarrossel3','title3','text3','published']

#HOME


def custom_home(request, template_name='dashboard-admin/custom/home.html'):
    
    home = get_object_or_404(PostHome)
    if request.method == "POST":
        form = HomeForm(request.POST, instance=home)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')
    else:
        form = HomeForm(instance=home)
    return render(request, template_name, {'form': form}) 

#END HOME



#SOBRE
def custom_sobre(request, template_name='dashboard-admin/custom/sobre.html'):

    sobre = get_object_or_404(PostQuemSomos)
    if request.method == "POST":
        form = SobreForm(request.POST, instance=sobre)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')
    else:
        form = SobreForm(instance=sobre)
    return render(request, template_name, {'form': form})


#END SOBRE

#NOTICIAS
def custom_noticias(request, template_name='dashboard-admin/custom/sobre.html'):

    noticias = get_object_or_404(PostNoticias)
    if request.method == "POST":
        form = NoticiasForm(request.POST, instance=noticias)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')
    else:
        form = NoticiasForm(instance=noticias)
    return render(request, template_name, {'form': form})


#END NOTICIAS

#END CUSTOM PAGES HOME, ASSINATURAS, APRENDER, SOBRE, NOTÍCIAS

#CUSTOM PAGES DASHBOARD HOME, ANÁLISES, VÍDEOS
class DashboardHomeForm(ModelForm):
    class Meta:
        model = Dashboard_home
        fields = ['image_header','text_header','link_header','noticias_hoje',
                    'link_noticias_hoje','bolsa_hoje','link_bolsa_hoje',]




class DashboardVideosForm(ModelForm):
    class Meta:
        model = Dashboard_videos
        fields = ['image_capa','titulo_capa','text_capa',
        'link_capa']


def custom_dashboard_home(request, template_name='dashboard-admin/custom/dashboard/home.html'):
    custom_home = get_object_or_404(Dashboard_home)
    if request.method == "POST":
        form = DashboardHomeForm(request.POST, instance=custom_home)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')
    else:
        form = DashboardHomeForm(instance=custom_home)
    return render(request, template_name, {'form': form})


def custom_dashboard_videos(request, template_name='dashboard-admin/custom/dashboard/videos.html'):
    videos = get_object_or_404(Dashboard_videos)
    if request.method == "POST":
        form = DashboardVideosForm(request.POST, instance=videos)
        if form.is_valid():
            form.save()
            return redirect('admin-dashboard')
    else:
        form = DashboardVideosForm(instance=videos)
    return render(request, template_name, {'form': form})
#END CUSTOM PAGES DASHBOARD HOME, ANÁLISES, VÍDEOS