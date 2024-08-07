from django.shortcuts import render
from django.http import HttpResponse
from utils.fake_recipes import create_fake_recipe

# Create your views here.

# django namespace: create template folder with child folder, if not, html files can conflit with each other
def home(request):
    return render(request, "recipes/pages/home.html", status=200, context= {
        'recipes': [create_fake_recipe() for _ in range(7)]
    })

def recipe(request, id):
    return render(request, "recipes/pages/recipe.html", status=200, context= { 'recipe': create_fake_recipe() })