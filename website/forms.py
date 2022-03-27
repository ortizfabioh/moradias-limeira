from django import forms
from posts.models import Post

# Definição dos campos do formulário de posts
class NewPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'description', 'image', 'repuPost')
        labels = {
            'author': 'Seu nome ',
            'description': 'Sua postagem ',
            'image': 'Tem alguma foto do local?',
            'repuPost': 'A vaga é em República?'
        }
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }
    # TODO permitir o upload de várias imagens
