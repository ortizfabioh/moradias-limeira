from django.forms import ModelForm, TextInput, Textarea, BooleanField, ImageField
from posts.models import Post

# Nome das variáveis é o label no HTML
class NewPostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'author', 'description', 'image', 'repuPost')
        labels = {
            'title': 'Título do post ',
            'author': 'Seu nome ',
            'description': 'Sua postagem ',
            'image': 'Tem alguma foto do local?',
            'repuPost': 'A vaga é em República?'
        }
    # TODO permitir o upload de várias imagens
