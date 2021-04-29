from django.shortcuts import render
from blog_noticias.models import Postpost

def blog(request):
    posts = Postpost.objects.all()
    return render(request, 'noticias.html', 'dashboard-noticias.html', {'posts':posts})

def post(request, post_id):
    post = Postpost.objects.get(pk=post_id)
    return render(request, 'post.html', {'post': post})