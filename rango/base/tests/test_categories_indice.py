import pytest
from django.urls import reverse
from model_bakery import baker

from rango.django_assertions import assert_contains
from rango.rangomain.models import Category, Page


@pytest.fixture
def category(db):
    return baker.make(Category)


@pytest.fixture
def pages(category):
    return baker.make(Page, 3, category=category)


@pytest.fixture
def resp(client, category, pages):
    resp = client.get(reverse('base:show_category', kwargs={'slug': category.slug}))
    return resp


def test_indice_disponivel(resp):
    assert resp.status_code == 200


def test_page_titulo(resp, pages):
    for page in pages:
        assert_contains(resp, page.titulo)
