from django.shortcuts import render
from .models import ReleasePost, ReleaseCategory

# Create your views here.
def releaseblog(request):

    context = {}
    posts = ReleasePost.objects.all()
    categories = Category.objects.all()

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