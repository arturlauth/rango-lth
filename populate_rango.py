import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'rango.settings')

import django

django.setup()
from rango.rangomain.models import Category, Page


def populate():
    python_cat = add_cat('Python - part 2', views=180, likes=64)

    add_page(cat=python_cat,
             titulo="Official Python Tutorial - part 2",
             url="https://docs.djangoproject.com/en/3.0/")

    add_page(cat=python_cat,
             titulo="How to Think like a Computer Scientist - part 2",
             url="https://docs.djangoproject.com/en/3.0/contents/")

    add_page(cat=python_cat,
             titulo="Learn Python in 10 Minutes - part 2",
             url="https://docs.djangoproject.com/en/3.0/intro/overview/#a-dynamic-admin-interface-it-s-not-just-scaffolding-it-s-the-whole-house")

    django_cat = add_cat("Django - part 2", views=90, likes=32)

    add_page(cat=django_cat,
             titulo="Official Django Tutorial - part 2",
             url="https://docs.djangoproject.com/en/3.0/intro/install/")

    add_page(cat=django_cat,
             titulo="Django Rocks - part 2",
             url="https://docs.djangoproject.com/en/3.0/intro/")

    add_page(cat=django_cat,
             titulo="How to Tango with Django - part 2",
             url="https://docs.djangoproject.com/en/3.0/intro/overview/")

    frame_cat = add_cat("Other Frameworks - part 2", views=40, likes=16)

    add_page(cat=frame_cat,
             titulo="Bottle - part 2",
             url="https://docs.djangoproject.com/en/3.0/py-modindex/")

    add_page(cat=frame_cat,
             titulo="Flask - part 2",
             url="https://docs.djangoproject.com/en/3.0/faq/")

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
