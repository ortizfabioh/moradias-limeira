from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NewPostForm
from posts.models import PostImages, Post

def about_page(request):
    context = {
        "title": "Página sobre",
        "content": "Bem-vindo a página sobre"
    }
    return render(request, "about/view.html", context)

def form_page(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('image')
        if form.is_valid():
            print(form.cleaned_data)
            author = form.cleaned_data["author"]
            description = form.cleaned_data["description"]
            data = Post.objects.create(author=author, description=description)
            for f in files:
                PostImages.objects.create(post=data, images=f)
            return HttpResponseRedirect("/posts/")
    else:
        form = NewPostForm()

    return render(request, "form/view.html", {"form": form})