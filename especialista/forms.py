from django import forms
from especialista.models import Comentario

class ChatCommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Insira sua mensagem',
        'rows':'4',
    }))

    class Meta:
        model  = Comentario
        fields = ('content',)