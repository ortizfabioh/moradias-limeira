from django.contrib import admin
from django.db.models import Count
from .models import Post, PostImages

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'slug', 'datePost', 'images_count', 'tags_count', 'repuPost', 'fbPost')

    class Meta:
        model = Post

    def images_count(self, obj):
        return obj.postimages_set.all().count()

    def tags_count(self, obj):
        return obj.tag.all().count()



class PostImagesAdmin(admin.ModelAdmin):
    class Meta:
        model = PostImages

admin.site.register(Post, PostAdmin)
admin.site.register(PostImages, PostImagesAdmin)