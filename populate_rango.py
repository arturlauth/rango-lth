import os

from django.template.defaultfilters import lower

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'rango.settings')

import django

django.setup()
from rango.rangomain.models import Category, Page


def populate():
    python_cat = add_cat('Python', views=128, likes=64)

    add_page(cat=python_cat,
             titulo="Official Python Tutorial",
             url="http://docs.python.org/2/tutorial/")

    add_page(cat=python_cat,
             titulo="How to Think like a Computer Scientist",
             url="http://www.greenteapress.com/thinkpython/")

    add_page(cat=python_cat,
             titulo="Learn Python in 10 Minutes",
             url="http://www.korokithakis.net/tutorials/python/")

    django_cat = add_cat("Django", views=64, likes=32)

    add_page(cat=django_cat,
             titulo="Official Django Tutorial",
             url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_page(cat=django_cat,
             titulo="Django Rocks",
             url="http://www.djangorocks.com/")

    add_page(cat=django_cat,
             titulo="How to Tango with Django",
             url="http://www.tangowithdjango.com/")

    frame_cat = add_cat("Other Frameworks", views=32, likes=16)

    add_page(cat=frame_cat,
             titulo="Bottle",
             url="http://bottlepy.org/docs/dev/")

    add_page(cat=frame_cat,
             titulo="Flask",
             url="http://flask.pocoo.org")

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f"{(str(c))} - {str(p)}")


def add_page(cat, titulo, url, views=0):
    p = Page.objects.get_or_create(category=cat, titulo=titulo, url=url, views=views)[0]
    return p


def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    return c


# Start execution here!
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
