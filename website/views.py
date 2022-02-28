from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import NewPostForm
from posts.views import PostListView, PostDetailView

def home_page(request):
    context = {
        "title": "Página principal",
        "content": "Bem-vindo a página principal"
    }
    return render(request, "home_page.html", context)

def about_page(request):
    context = {
        "title": "Página sobre",
        "content": "Bem-vindo a página sobre"
    }
    return render(request, "about/view.html", context)

def form_page(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            title = form.cleaned_data["title"]
            author = form.cleaned_data["author"]
            description = form.cleaned_data["description"]
            form.save()
            return HttpResponseRedirect("/posts/")
    else:
        form = NewPostForm()

    return render(request, "form/view.html", {"form": form})