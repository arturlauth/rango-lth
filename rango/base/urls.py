from django.urls import path

from rango.base import views

app_name = 'base'
urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:slug>', views.show_category, name='show_category')
]
