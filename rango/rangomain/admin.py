from django.contrib import admin

from ordered_model.admin import OrderedModelAdmin

from rango.rangomain.models import Page, Category


@admin.register(Category)
class CategoryAdmin(OrderedModelAdmin):
    list_display = ('name', 'views', 'likes', 'move_up_down_links')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Page)
class PageAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'category', 'url')
