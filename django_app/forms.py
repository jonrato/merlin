from django import forms
from django_app.models import Comment_Assinaturas

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Insira seu comentário',
        'rows':'4',
    }))

    class Meta:
        model  = Comment_Assinaturas
        fields = ('content',)