from django import forms
from blog_noticias.models import Comment

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Insira seu comentário',
        'rows':'4',
    }))

    class Meta:
        model  = Comment
        fields = ('content',)