from django.shortcuts import render
from django.http import HttpResponse
from .models import *

## home page view
def home(request):
    pass



## all recipes page view
def recipes(request):
    recipes = Recipe.objects.all()
    context = {
        'recipes':recipes,

    }
    return render(request, 'main/recipes.html', context)


## repies details page view
def details(request, pk):
    details = Recipe.objects.get(id=pk)
    context = {
        'details':details,

    }
    return render(request, 'main/details.html', context)
