from django.db.models import Q
from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.urls import reverse

class PostQuerySet(models.query.QuerySet):
    def fbPost(self):
        return self.filter(fbPost = True)

    # Retornar posts de Repúblicas
    def repuPost(self):
        return self.filter(repuPost = True)
    
    # Retornar posts q não são de Repúblicas
    def commonPost(self):
        return self.filter(repuPost = False)

    # Retornar posts q encaixam na busca
    def search(self, query):
        lookups = (
            Q(description__contains = query) | 
            Q(author__contains = query) |
            Q(tag__title__contains = query))
        return self.filter(lookups).distinct()
    

class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using = self._db)

    def repuPost(self):
        return self.get_queryset().repuPost()
    
    def commonPost(self):
        return self.get_queryset().commonPost()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id = id)
        if qs.count() == 1:
            return qs.first()
        return None
    
    def search(self, query):
        return self.get_queryset().search(query)

class Post(models.Model):
    slug        = models.SlugField(blank=True, max_length=120, unique=True)
    author      = models.CharField(max_length=120)
    description = models.TextField()
    datePost    = models.DateTimeField(auto_now_add=True)  # auto_now_add=True salva a hora de criação e deixa imutável
    image       = models.ImageField(upload_to='posts/', blank=True, null=True)
    repuPost    = models.BooleanField(default = False)
    fbPost      = models.BooleanField(default = False)

    objects = PostManager()

    class Meta:
        ordering = ("-datePost",)

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})


class PostImages(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='posts/')


def post_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(post_pre_save_receiver, sender = Post)