# Create your views here.
from django.shortcuts import render

from rango.base import facade
from rango.base.forms import CategoryForm, PageForm


def home(request):
    categories = facade.listar_categorias_ordenadas_likes()
    pages = facade.listar_pages_ordenadas_views()
    return render(request, 'base/home.html', context={'pages': pages, 'categories': categories})


def show_category(request, slug):
    categories = facade.encontrar_categorias(slug)
    pages = facade.listar_paginas_de_category_ordenadas(categories)
    return render(request, 'base/category.html', context={'categories': categories, 'pages': pages})


def add_category(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = CategoryForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return home(request)

        else:
            print(form.errors)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CategoryForm()

    return render(request, 'base/add_category.html', {'form': form})


def add_page(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.clean()
            form.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return home(request)

        else:
            print(form.errors)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PageForm()

    return render(request, 'base/add_page.html', {'form': form})
