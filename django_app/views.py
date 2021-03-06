from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django_app.models import Author_Assinaturas, Category_Assinaturas, Comment_Assinaturas, Home, Post_Assinaturas, Cursos
from admindashboard.models import PostHome
from hitcount.views import HitCountDetailView
from django_app.forms import CommentForm, CursosForm, AssinaturaForm
from django.forms import ModelForm


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
from django.db.models import Q, query
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
from cart.models import Cart

class APostDetailView(ObjectViewMixin, HitCountDetailView,):
    model = Post_Assinaturas
    template_name = "assinaturas_post.html"
    slug_field = "slug"
    def get_context_data(self,*args, **kwargs):
        context = super(APostDetailView, self).get_context_data(*args,**kwargs)
        cart_obj,new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

    
#    count_hit = True

    

#CRUD ASSINATURAS
def index_assinaturas(request):
    
    return render(request, 'dashboard-admin/assinaturas/a.html')



#END CRUD ASSINATURAS
from django.forms import ModelForm
class AuthorForm(ModelForm):
    class Meta:
        model = Author_Assinaturas
        fields = ['user','profile_image']

class CategoriaForm(ModelForm):
    class Meta:
        model = Category_Assinaturas
        fields = ['title']

class AssinaturaForm(ModelForm):
    class Meta:
        model = Post_Assinaturas
        fields = ['title','preco','overview', 'content','author','categories','images','published']




#Cadastrar Assinatura

def cadastrar_assinatura(request, template_name="dashboard-admin/assinaturas/assinatura_form-upload.html"):
    form = AssinaturaForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('listar_assinatura')
    return render(request, template_name, {'form':form})

def listar_assinatura(request, template_name="dashboard-admin/assinaturas/assinatura_list.html"):
    query = request.GET.get("busca")
    if query:
        assinatura = Post_Assinaturas.objects.filter(title__contains=query)
    else:
        assinatura = Post_Assinaturas.objects.all()
    
    assinaturas = {'lista': assinatura}
    return render(request, template_name, assinaturas)

def editar_assinatura(request, pk, template_name='dashboard-admin/assinaturas/assinatura_form-upload.html'):
    assinatura = get_object_or_404(Post_Assinaturas, pk=pk)
    if request.method == "POST":
        form = AssinaturaForm(request.POST, request.FILES or None, instance=assinatura)
        if form.is_valid():
            form.save()
            return redirect('listar_assinatura')
    else:
        form = AssinaturaForm(instance=assinatura)
    return render(request, template_name, {'form': form})

def remover_assinatura(request, pk, template_name='dashboard-admin/assinaturas/assinatura_delete.html'):
    assinatura = Post_Assinaturas.objects.get(pk=pk)
    if request.method == "POST":
        assinatura.delete()
        return redirect('listar_assinatura')
    return render(request, template_name, {'assinatura': assinatura})

def listar_autor_assinatura(request, pk, template_name="dashboard-admin/assinaturas/autor_assinaturas_list.html"):
    autores = Post_Assinaturas.objects.filter(author = pk)
    return render(request, template_name, {'autores': autores})

def cadastrar_autor(request, template_name='dashboard-admin/assinaturas/autor_form-upload.html'):
    form =  AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_autor')
    return render(request, template_name, {'form': form})

def listar_autor(request, template_name="dashboard-admin/assinaturas/autor_list.html"):
    query = request.GET.get("busca")
    if query:
        autor = Author_Assinaturas.objects.filter(descricao__iexact=query)
    else:
        autor = Author_Assinaturas.objects.all()
    autores = {'lista': autor}
    return render(request, template_name, autores)

def perfil_autor(request, pk, template_name="dashboard-admin/assinaturas/autor_show.html"):
    autor = get_object_or_404(Author_Assinaturas, pk=pk)
    return render(request, template_name, {'autor':autor})

def editar_autor(request, pk, template_name='dashboard-admin/assinaturas/autor_form.html'):
    autor = get_object_or_404(Author_Assinaturas, pk=pk)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('listar_autor')
    else:
        form  = AuthorForm(instance=autor)
    return render(request, template_name, {'form':form})

def remover_autor(request, pk, template_name='dashboard-admin/assinaturas/autor_delete.html'):
    autor = Author_Assinaturas.objects.get(pk=pk)
    if request.method == "POST":
        autor.delete()
        return redirect('listar-autor')
    return render(request, template_name, {'autor':autor})

def cadastrar_categoria(request, template_name='dashboard-admin/assinaturas/categoria_form.html'):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_categoria')
    return render(request, template_name, {'form':form})

def listar_categoria(request, template_name="dashboard-admin/assinaturas/categoria_list.html"):
    query = request.GET.get("busca")
    if query:
        categoria = Category_Assinaturas.objects.filter(title__contains=query)
    else:
        categoria = Category_Assinaturas.objects.all()
    categoria = {'lista':categoria}
    return render(request, template_name, categoria)

def editar_categoria(request, pk, template_name='dashboard-admin/assinaturas/categoria_form.html'):
    categoria = get_object_or_404(Category_Assinaturas, pk=pk)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('listar_categoria')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, template_name, {'form':form})

def remover_categoria(request, pk, template_name='dashboard-admin/assinaturas/categoria_delete.html'):
    categoria = Category_Assinaturas.objects.get(pk=pk)
    if request.method == "POST":
        categoria.delete()
        return redirect('listar_assinatura')
    return render(request, template_name, {'categoria':categoria})

def listar_assinaturas_categoria(request, pk, template_name="dashboard-admin/assinaturas/categoria_assinaturas_list.html"):
    assinaturas = Post_Assinaturas.objects.filter(categories = pk)
    categoria = get_object_or_404(Category_Assinaturas, pk=pk)
    return render(request, template_name, {'assinaturas':assinaturas,'categoria':categoria})





#end assinaturas

#Cursos
class PostList(ListView):
        model = Cursos

def index_curso(request):
    cursos_show = Cursos.objects.all()
    context = {'cursos_show': cursos_show}
    return render(request, 'dashboard-admin/cursos/produtos.html', context)


#Cadastrar, Editar, Deletar Postagens
def cadastrar_curso(request, template_name="dashboard-admin/cursos/curso_form-upload.html"):
    form = CursosForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index_curso')
    return render(request, template_name, {'form':form})


def editar_curso(request, pk, template_name='dashboard-admin/cursos/curso_form-upload.html'):
    cursos_show = get_object_or_404(Cursos, pk=pk)
    if request.method == "POST":
        form = CursosForm(request.POST or None, request.FILES or None, instance=cursos_show)
        if form.is_valid():
            form.save()
            return redirect('index_curso')
    else:
        form = CursosForm(instance=cursos_show)
    return render(request, template_name, {'form': form})

def remover_curso(request, pk, template_name='dashboard-admin/cursos/curso_delete.html'):
    cursos_show = Cursos.objects.get(pk=pk)
    if request.method == "POST":
        cursos_show.delete()
        return redirect('index_curso')
    return render(request, template_name, {'cursos_show': cursos_show})

#END Cursos