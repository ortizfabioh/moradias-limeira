from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'slug', 'datePost', 'image', 'repuPost', 'fbPost')

    class meta:
        model = Post

admin.site.register(Post, PostAdmin)