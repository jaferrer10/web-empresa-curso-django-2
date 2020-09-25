from django.shortcuts import render, get_list_or_404
from .models import Post, Category

# Create your views here.
def blog(request):

    #Guarda en una variable, todos los elementos formando una lista, y luego en el return devuelve un diccionario de datos
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {'posts': posts})


def category(request, category_id):
    category = get_list_or_404(Category, id=category_id)
    posts = Post.objects.filter(categories=category_id)
    return render(request, "blog/category.html", {'category':category, 'posts':posts})
