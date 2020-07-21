import pytest
from model_bakery import baker

from rango.base import facade
from rango.rangomain.models import Category


@pytest.fixture
def categories(db):
    return [baker.make(Category, name=s) for s in 'Antes Depois'.split()]


def test_listar_categorias_ordenadas(categories):
    assert list(sorted(categories, key=lambda categories: categories.likes)) == facade.listar_categorias_ordenadas()
