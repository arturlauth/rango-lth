from typing import List

from rango.rangomain.models import Category, Page


def listar_categorias_ordenadas() -> List[Category]:
    return list(Category.objects.order_by('-likes').all())


def encontrar_categorias(slug: str) -> Category:
    return Category.objects.get(slug=slug)


def encontrar_paginas(slug):
    return Page.objects.select_related('category').get(slug=slug)


def listar_paginas_de_category_ordenadas(category: Category):
    return list(category.page_set.order_by('order').all())
