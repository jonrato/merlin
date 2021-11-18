from .models import *
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render, redirect
from videos.forms import PostForm
# Create your views here.
#Cursos
class PostList(ListView):
        model = Post

def index_video(request):
    video = Post.objects.all()
    context = {'video': video}
    return render(request, 'dashboard-admin/videos/videos-admin.html', context)


#Cadastrar, Editar, Deletar Postagens
def cadastrar_video(request, template_name="dashboard-admin/videos/videos_form-upload.html"):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index_curso')
    return render(request, template_name, {'form':form})


def editar_video(request, pk, template_name='dashboard-admin/videos/videos_form-upload.html'):
    video = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST or None, request.FILES or None, instance=video)
        if form.is_valid():
            form.save()
            return redirect('index_curso')
    else:
        form = PostForm(instance=video)
    return render(request, template_name, {'form': form})

def remover_video(request, pk, template_name='dashboard-admin/videos/videos_delete.html'):
    video = Post.objects.get(pk=pk)
    if request.method == "POST":
        video.delete()
        return redirect('index_curso')
    return render(request, template_name, {'video': video})

#END Cursos