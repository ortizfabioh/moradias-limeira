from attr import attr
from django.forms import ImageField, ModelForm
from posts.models import Post

class NewPostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('author', 'description', 'image', 'repuPost')
        labels = {
            'author': 'Seu nome ',
            'description': 'Sua postagem ',
            'image': 'Tem alguma foto do local?',
            'repuPost': 'A vaga é em República?'
        }
    # TODO permitir o upload de várias imagens
