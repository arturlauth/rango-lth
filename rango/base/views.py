# Create your views here.
from django.shortcuts import render

from rango.base import facade


def home(request):
    categories = facade.listar_categorias_ordenadas()
    return render(request, 'base/home.html', context={'categories': categories})


def show_category(request, slug):
    categories = facade.encontrar_categorias(slug)
    pages = facade.listar_paginas_de_category_ordenadas(categories)
    return render(request, 'base/category.html', context={'categories': categories, 'pages': pages})
