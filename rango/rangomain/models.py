from django.db import models

from ordered_model.models import OrderedModel
from django.utils.text import slugify


class Category(OrderedModel):
    name = models.CharField(max_length=64)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta(OrderedModel.Meta):
        verbose_name_plural = 'categories'
        ordering = ('name',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Page(OrderedModel):
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=64)
    url = models.URLField()
    views = models.IntegerField(default=0)
    order_with_respect_to = 'category'

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.titulo
