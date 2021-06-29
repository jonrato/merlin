from especialista.models import Chat, Comentario
from django.forms.models import ModelForm
from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator,PageNotAnInteger, EmptyPage
from history.mixins import ObjectViewMixin
from hitcount.views import HitCountDetailView
from especialista.forms import ChatCommentForm

class PostForm(ModelForm):
    class Meta:
        model = Chat
        fields = ['assunto','mensagem']





class PList(ListView):
        model = Chat

def Chatblog(request):
    context = {}
    
    chats = Chat.objects.all()
    
    

    page = request.GET.get("page")
    paginator = Paginator(chats, 4)
    try:
        chats = paginator.page(page)
    except PageNotAnInteger:
        chats = paginator.page(1)
    except EmptyPage:
        chats = paginator.page(paginator.num_pages)

    context = {
        
        
        
        'chats': chats,
    }

    return render(request, "especialista/post_list.html",context)

class DetailView(ObjectViewMixin, HitCountDetailView):
    model = Chat
    template_name = "chat.html"
    slug_field = "slug"
    
    

    form = ChatCommentForm

    def post(self, request, *args, **kwargs):
        form = ChatCommentForm(request.POST)
        if form.is_valid():
            post = self.get_object()
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect(reverse("chat_post", kwargs={
                'slug': post.slug
            }))
    def get_context_data(self, **kwargs):
        post_comments_count = Comentario.objects.all().filter(post=self.object.id).count()
        post_comments = Comentario.objects.all().filter(post=self.object.id)
        context = super().get_context_data(**kwargs)
        context.update({
            'form': self.form,
            'post_comments': post_comments,
            
        })

        return context 