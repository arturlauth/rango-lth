from django.contrib import admin

# Register your models here.
from rango.rangomain.models import Page, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass
