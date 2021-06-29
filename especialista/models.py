from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect, reverse

User = get_user_model()


class Chat(models.Model):
    assunto = models.CharField(max_length=200)
    slug = AutoSlugField(populate_from='assunto')
    mensagem = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    

    @property
    def chat_link(self):
        return reverse("chat_post", kwargs={
            'slug':self.slug
        })
    
    def get_absolute_url(self):
        return reverse('chat_post', kwargs={'pk': self.pk})


    def __str__(self):
        return self.assunto


class Comentario(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    post = models.ForeignKey('Chat', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.user.username
