from django.http import HttpResponse
from django.shortcuts import render
from .forms import NewPostForm

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
    post_form = NewPostForm(request.POST or None)
    context = {
        "title": "Página de formulário",
        "content": "Bem-vindo a página de formulário",
        "form": post_form
    }
    if post_form.is_valid():
        print(post_form.cleaned_data)
    #if request.method == "POST":
        #print(request.POST)
        #print(request.POST.get('identification'))
        #print(request.POST.get('contact'))
        #print(request.POST.get('post'))
    return render(request, "form/view.html", context)