from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic, View
from .models import Recipe
from .forms import RecipeForm


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.all()
    list_recipe = queryset
    template_name = 'recipe.html'
    paginate_by = 6


# def recipe(request):
#     list_recipe = Recipe.objects.all()
#     return render(request, "recipe.html", {'list_recipe': list_recipe})


def create_recipe(request):
    user = request.user
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES)
        print(request.FILES)
        if recipe_form.is_valid():
            recipe_form.instance.author = user
            recipe_form.instance.status = 1
            recipe_form.save()
            return redirect(home)
    return render(request, "create_recipe.html", {'form': RecipeForm})


def home(request):
    return render(request, "index.html")


def signup(request):
    return render(request, "signup.html")


def login(request):
    return render(request, "login.html")
