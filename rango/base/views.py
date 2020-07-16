# Create your views here.
from django.shortcuts import render


def home(request):
    context_dict = {'boldmessage': "Meow, meow, meow"}
    return render(request, 'base/home.html', context=context_dict)
