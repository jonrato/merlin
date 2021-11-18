from django.shortcuts import render
from .models import ReleasePost, ReleaseCategory
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect


# Create your views here.
def releaseblog(request):

    context = {}
    posts = ReleasePost.objects.all()
    categories = ReleaseCategory.objects.all()

    page = request.GET.get("page")
    paginator = Paginator(posts, 5)
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

    return render(request, "release_noticias/post_list.html",context)


#Release
class PostList(ListView):
        model = ReleasePost

def index_release(request):
    release = ReleasePost.objects.all()
    context = {'release': release}
    return render(request, 'dashboard-admin/release/index_release.html', context)


#Cadastrar, Editar, Deletar Postagens
def cadastrar_release(request, template_name="dashboard-admin/release/release_form-upload.html"):
    form = ReleaseForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index_release')
    return render(request, template_name, {'form':form})


def editar_release(request, pk, template_name='dashboard-admin/release/release_form-upload.html'):
    release = get_object_or_404(ReleasePost, pk=pk)
    if request.method == "POST":
        form = ReleaseForm(request.POST or None, request.FILES or None, instance=release)
        if form.is_valid():
            form.save()
            return redirect('index_release')
    else:
        form = ReleaseForm(instance=release)
    return render(request, template_name, {'form': form})

def remover_release(request, pk, template_name='dashboard-admin/release/release_delete.html'):
    release = ReleasePost.objects.get(pk=pk)
    if request.method == "POST":
        release.delete()
        return redirect('index_release')
    return render(request, template_name, {'release': release})

#END Release

#categoria
from django.forms.models import ModelForm

class ReleaseForm(ModelForm):
    class Meta:
        model = ReleasePost
        fields = ['title','thumbnail', 'image_url', 'overview',
                'categorias','published']

class ReleaseCategoriaForm(ModelForm):
    class Meta:
        model = ReleaseCategory
        fields = ['title']

def cadastrar_release_categoria(request, template_name="dashboard-admin/release/categoria_form.html"):
    form = ReleaseCategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index_release')
    return render(request, template_name, {'form':form})


def listar_release_categoria(request, template_name="dashboard-admin/release/categoria_list.html"):
    query = request.GET.get("busca")
    if query:
        categoria = ReleaseCategory.objects.filter(title__contains=query)
    else:
        categoria = ReleaseCategory.objects.all()
    categoria = {'lista':categoria}
    return render(request, template_name, categoria)

def editar_release_categoria(request, pk, template_name='dashboard-admin/release/categoria_form.html'):
    categoria = get_object_or_404(ReleaseCategory, pk=slug)
    if request.method == "POST":
        form = ReleaseCategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('index_release')
    else:
        form = ReleaseCategoriaForm(instance=categoria)
    return render(request, template_name, {'form': form})

def remover_release_categoria(request, pk, template_name='dashboard-admin/release/categoria_delete.html'):
    categoria = ReleaseCategory.objects.get(pk=pk)
    if request.method == "POST":
        categoria.delete()
        return redirect('index_release')
    return render(request, template_name, {'categoria': categoria})