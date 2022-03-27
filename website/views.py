from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NewPostForm
from posts.models import PostImages, Post

# Validação do formulário de posts
def form_page(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('image')
        if form.is_valid():
            print(form.cleaned_data)
            author = form.cleaned_data["author"].strip('\n')
            description = form.cleaned_data["description"].strip('\n')
            repuPost = form.cleaned_data["repuPost"]
            data = Post.objects.create(author=author, description=description, repuPost=repuPost)
            for f in files:
                PostImages.objects.create(post=data, images=f)
            return HttpResponseRedirect("/posts/")
    else:
        form = NewPostForm()

    return render(request, "form/view.html", {"form": form})