from django.core import paginator
from django.db.models import query
from django.shortcuts import render, redirect, reverse
from django.views.generic.detail import DetailView
from blog_noticias.models import Category, Comment, Post
from hitcount.views import HitCountDetailView
from blog_noticias.forms import CommentForm
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
from django.db.models import Q


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

def blog(request):

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

    return render(request, "noticias.html",context)

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