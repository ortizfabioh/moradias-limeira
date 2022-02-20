from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'datePost', 'image', 'repuPost', 'fbPost')
    prepopulated_fields = {"slug": ("title",)}

    class meta:
        model = Post

admin.site.register(Post, PostAdmin)