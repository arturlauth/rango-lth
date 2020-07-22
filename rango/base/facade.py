from typing import List

from rango.rangomain.models import Category, Page


def listar_pages_ordenadas_views() -> List[Category]:
    return list(Page.objects.order_by('-views').all()[:5])


def listar_categorias_ordenadas_likes() -> List[Category]:
    return list(Category.objects.order_by('-likes').all()[:5])


def encontrar_categorias(slug: str) -> Category:
    return Category.objects.get(slug=slug)


def encontrar_paginas(slug):
    return Page.objects.select_related('category').get(slug=slug)


def listar_paginas_de_category_ordenadas(category: Category):
    return list(category.page_set.order_by('-views').all())
