from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import HttpResponseRedirect
from django.views import generic, View
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm


class RecipeList(generic.ListView):
    """
    class that creates the recipe list
    """
    model = Recipe
    queryset = Recipe.objects.all()
    list_recipe = queryset
    template_name = 'recipe.html'
    paginate_by = 6


class RecipeDetail(View):
    """
    creates single recipe view
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        function that enables post comments 
        """
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class RecipeLike(View):
    """
    class that allows user to like recipe
    """
    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def create_recipe(request):
    """
    function that enables user to create recipe
    """  
    user = request.user
    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES)
        print(request.FILES)
        if recipe_form.is_valid():
            recipe_form.instance.author = user
            recipe_form.instance.status = 1
            recipe_form.save()
            return redirect('home')
    return render(request, "create_recipe.html", {'form': RecipeForm})


def edit_recipe(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    recipe_form = RecipeForm(request.POST or None, instance=recipe)

    if request.method == "POST":
        recipe_form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()
        return redirect('home')
    else:
        recipe_form = RecipeForm(instance=recipe)
    context = {
        "recipe_form": recipe_form,
        "recipe": recipe
    }
    return render(request, "edit_recipe.html", context)


def delete_recipe(request, slug):
    """
    function that enables user to delete recipe
    """    
    context = {}
    recipe = get_object_or_404(Recipe, slug=slug)

    if request.method == "POST":
        recipe.delete()
        return HttpResponseRedirect("/")

    return render(request, "delete_recipe.html", context)


def home(request):
    """
    function renders signup page
    """    
    return render(request, "index.html")


def signup(request):
    """
    function renders signup page
    """    
    return render(request, "signup.html")


def login(request):
    """
    function renders login page
    """    
    return render(request, "login.html")
