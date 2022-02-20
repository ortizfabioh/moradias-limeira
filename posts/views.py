# from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import Http404
from .models import Post

# Views somente de posts de repúblicas
class RepuPostListView(ListView):
    template_name = "posts/list.html"

    def get_queryset(self, *args, **kwargs):
        return Post.objects.repuPost()

class RepuPostDetailView(DetailView):
    queryset = Post.objects.all().repuPost()
    template_name = "posts/RepuPost-detail.html"



# Views comuns
class PostListView(ListView):
    queryset = Post.objects.all()
    template_name = 'posts/list.html'

class PostDetailView(DetailView):
    template_name = "posts/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context
    
    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        try:
            instance = Post.objects.get(slug = slug)
        except Post.DoesNotExist:
            raise Http404("Não encontrado!")
        except Post.MultipleObjectsReturned:
            qs = Post.objects.filter(slug = slug, RepuPost=True)
            instance = qs.first()
        return instance