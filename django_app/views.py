from django.shortcuts import render
from django.http import HttpResponse
from django_app.models import Category_Assinaturas, Comment_Assinaturas, Home, Post_Assinaturas
from admindashboard.models import PostHome
from hitcount.views import HitCountDetailView
from django_app.forms import CommentForm

#home
def index(request):

    context = {}
    posts = PostHome.objects.all()
    
    context = {
        
        'posts': posts,
    }
    return render(request, 'home.html', context)

def index_admin(request):

    context = {}
    posts = PostHome.objects.all()
    
    context = {
        
        'posts': posts,
    }
    return render(request, 'dashboardadmin/index.html', context)

class PostDetailView(HitCountDetailView):
    model = PostHome
    template_name = "home.html"
    count_hit = True

def home(request, home_id):
    home = Home.objects.get(pk=home_id)
    return render(request, 'home.html', {'home': home})
#end home

#assinaturas
from django_app.models import Post_Assinaturas
from history.mixins import ObjectViewMixin
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect, reverse

class AssinaturasList(ListView):
    model = Post_Assinaturas



def Assinaturas(request):

    context = {}
    
    posts_assinturas = Post_Assinaturas.objects.all()
    categories = Category_Assinaturas.objects.all()
    #popular_posts = Post_Assinaturas.objects.order_by('-hit_count_generic')[:4]

    page = request.GET.get("page")
    paginator = Paginator(posts_assinturas, 4)
    try:
        aposts = paginator.page(page)
    except PageNotAnInteger:
        aposts = paginator.page(1)
    except EmptyPage:
        aposts = paginator.page(paginator.num_pages)

    context = {
        
        #'popular_posts':popular_posts,
        'categories':categories,
        'aposts': aposts,
    }

    return render(request, "django_app/post_assinaturas_list.html",context)

class APostDetailView(ObjectViewMixin, HitCountDetailView):
    model = Post_Assinaturas
    template_name = "assinaturas_post.html"
    slug_field = "slug"
#    count_hit = True

    




def assinaturas(request):
    acount = Assinaturas.objects.all().count()
    return render(request, 'django_app/dashboardadmin/index.html', {'assinaturas': assinaturas})

#end assinaturas

