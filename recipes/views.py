from django.shortcuts import render
from django.views import generic, View
from .models import Recipe



class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


def recipe(request):
    """
    renders recipe page
    """
    return render(request, "recipe.html")

def create_recipe(request):
  
    return render(request, 'create_recipe.html')


def signup(request):
    """
    renders signup page
    """
    return render(request, "signup.html")


def login(request):
    """
    renders login page
    """
    return render(request, "login.html")
