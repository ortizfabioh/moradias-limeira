from django.db import models
from django.contrib.auth.models import User
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.urls import reverse

class PostQuerySet(models.query.QuerySet):
    def fbPost(self):
        return self.filter(fbPost = True)

    # Retornar só posts de Repúblicas
    def repuPost(self):
        return self.filter(repuPost = True)
    
    # Retornar só posts q não são de Repúblicas
    def post(self):
        return self.filter(repuPost = False)

class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using = self._db)
    
    def all(self):
        return self.get_queryset().post()

    def repuPost(self): # Criando uma query personalizada para chamar posts repu (Q são de repúblicas)
        return self.get_queryset().repuPost()
    
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id = id)
        if qs.count() == 1:
            return qs.first()
        return None

class Post(models.Model):
    title       = models.CharField(max_length=120)
    slug        = models.SlugField(blank=True, max_length=120, unique=True)
    author      = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    description = models.TextField()
    datePost    = models.DateTimeField(auto_now_add=True)  # auto_now_add=True salva a hora de criação e deixa imutável
    image       = models.ImageField(upload_to='posts/', null=True, blank=True)
    repuPost    = models.BooleanField(default = False)
    fbPost      = models.BooleanField(default = False)

    objects = PostManager()

    class Meta:
        ordering = ("-datePost",)

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})  # dinâmico
        return "/posts/{slug}/".format(slug = self.slug)  # hard code

    def __str__(self):
        return self.title

def post_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(post_pre_save_receiver, sender = Post)