from . import views
from django.urls import path
from .views import RecipeList, RecipeDetail, delete_recipe


urlpatterns = [
    path('', views.home, name='home'),
    path('create_recipe', views.create_recipe, name='create_recipe'),
    path('signup', views.signup, name='signup'),
    path('recipe', RecipeList.as_view(), name='recipe'),
    path('<slug:slug>/', RecipeDetail.as_view(), name='recipe_detail'),
    path('login', views.login, name='login'),
    path('edit/<slug:slug>', views.edit_recipe, name='edit_recipe'),
    path('delete/<slug:slug>', views.delete_recipe, name='delete_recipe')
    
]