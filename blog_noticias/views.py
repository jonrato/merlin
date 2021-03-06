from django.core import paginator
from django.db.models import query
from django.forms.models import ModelForm
from django.shortcuts import render, redirect, reverse
from django.views.generic.detail import DetailView
from blog_noticias.models import Author, Category, Comment, Post
from admindashboard.models import PostNoticias
from hitcount.views import HitCountDetailView
from blog_noticias.forms import CommentForm
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
from django.db.models import Q


from django.views.generic import ListView, DetailView
from history.mixins import ObjectViewMixin
from django.shortcuts import get_object_or_404


def boracontar(request,self):
    
    contar = Post.objects.all()
    cont = contar.count()
    context = {
        'cont': cont
    }
    return render(request,'dashboard-admin/index.html',context)


#dashboard noticias
from django.contrib.auth.decorators import login_required
@login_required(login_url='/login')
def noticia(request):

    context = {}
    posts = Post.objects.all()
    categories = Category.objects.all()

    page = request.GET.get("page")
    paginator = Paginator(posts, 4)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'categories':categories,
        'posts': posts,
    }

    return render(request, "dashboard-noticias.html",context)

#end dashboard noticias

def searchBlog(request):
    context = {}
    posts = Post.objects.all()
    if request.method == "GET":
        query = request.GET.get("search")
        queryset = posts.filter(Q(title__icontains=query))

        page = request.GET.get("page")
        paginator = Paginator(queryset, 2)
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)
        total = queryset.count()
        context.update({
            
            "page":page,
            "total":total,
            "query":query,
            "posts":posts,
            
        })

        return render(request, "search.html", context)

class PostList(ListView):
        model = Post

def blog(request):
    


    context = {}
    carrossel = PostNoticias.objects.all()
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
        'carrossel': carrossel,
        'popular_posts':popular_posts,
        'categories':categories,
        'posts': posts,
    }

    return render(request, "blog_noticias/post_list.html",context)

class PostDetailView(HitCountDetailView):
    model = Post
    template_name = "post.html"
    slug_field = "slug"
    count_hit = True
    form = CommentForm
    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("post", kwargs={
                'slug': post.slug
            }))
    def get_context_data(self, **kwargs):
        post_comments_count = Comment.objects.all().filter(post=self.object.id).count()
        post_comments = Comment.objects.all().filter(post=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form,
            'post_comments': post_comments,
            'post_comments_count': post_comments_count,
        })

        return context

        


#CRUD NOT??CIAS


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ['user']

class CategoriaForm(ModelForm):
    class Meta:
        model = Category
        fields = ['title']

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','thumbnail','overview','content','author','categories','published','favorite']


#Cadastrar, Editar, Deletar Postagens
def cadastrar_noticia(request, template_name="dashboard-admin/noticias/noticia_form-upload.html"):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('artigos-dashboard')
    return render(request, template_name, {'form':form})


def editar_noticia(request, pk, template_name='dashboard-admin/noticias/noticia_form-upload.html'):
    noticia = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('artigos-dashboard')
    else:
        form = PostForm(instance=noticia)
    return render(request, template_name, {'form': form})

def remover_noticia(request, pk, template_name='dashboard-admin/noticias/noticia_delete.html'):
    noticia = Post.objects.get(pk=pk)
    if request.method == "POST":
        noticia.delete()
        return redirect('artigos-dashboard')
    return render(request, template_name, {'noticia': noticia})

#Coment??rios Not??cias
def listar_comentario(request, template_name="dashboard-admin/noticias/comentario_list.html"):
    query = request.GET.get("busca")
    if query:
        comentario = Comment.objects.filter(title__contains=query)
    else:
        comentario = Comment.objects.all()
    
    comentarios = {'lista': comentario}
    return render(request, template_name, comentarios)

def remover_comentario(request, pk, template_name='dashboard-admin/assinaturas/assinatura_delete.html'):
    comentario = Comment.objects.get(pk=pk)
    if request.method == "POST":
        comentario.delete()
        return redirect('listar_comentario')
    return render(request, template_name, {'comentario': comentario})


#categoria
def cadastrar_noticia_categoria(request, template_name="dashboard-admin/noticias/categoria_form.html"):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('artigos-dashboard')
    return render(request, template_name, {'form':form})


def listar_noticia_categoria(request, template_name="dashboard-admin/noticias/categoria_list.html"):
    query = request.GET.get("busca")
    if query:
        categoria = Category.objects.filter(title__contains=query)
    else:
        categoria = Category.objects.all()
    categoria = {'lista':categoria}
    return render(request, template_name, categoria)

def editar_noticia_categoria(request, pk, template_name='dashboard-admin/noticias/categoria_form.html'):
    categoria = get_object_or_404(Category, pk=slug)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('artigos-dashboard')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, template_name, {'form': form})

def remover_noticia_categoria(request, pk, template_name='dashboard-admin/noticias/categoria_delete.html'):
    categoria = Post.objects.get(pk=pk)
    if request.method == "POST":
        categoria.delete()
        return redirect('artigos-dashboard')
    return render(request, template_name, {'categoria': categoria})