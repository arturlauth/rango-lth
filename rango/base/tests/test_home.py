import pytest
from django.urls import reverse
from model_bakery import baker

from rango.django_assertions import assert_contains
from rango.rangomain.models import Category


@pytest.fixture
def categories(db):
    return baker.make(Category, 2)


@pytest.fixture
def resp(client, categories):
    resp = client.get(reverse('base:home'))
    return resp


def test_status_code(resp):
    assert resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Rango</title>')


def test_image_shown(resp):
    assert_contains(resp, '<img src="')


def test_nome_das_categorias(resp, categories):
    for categoria in categories:
        assert_contains(resp, categoria.name)
