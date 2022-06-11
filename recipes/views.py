from django.shortcuts import render
from django.views import generic, View
from .models import Recipe
from .forms import RecipeForm


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by("-created_on")
    template_name = "recipe.html"
    paginate_by = 6

def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
    elif form.is_valid():
        form.save()
        return redirect('')
    else:
        return render(request, 'create_recipe.html', {"form":form})
    

def home(request):
    return render(request, "index.html")

def recipe(request):
    return render(request, "recipe.html")

def create_recipe(request):
    return render(request, 'create_recipe.html')


def signup(request):
    return render(request, "signup.html")


def login(request):
    return render(request, "login.html")
