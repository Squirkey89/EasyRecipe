from . import views 
from django.urls import path
from .views import RecipeList


urlpatterns = [
    path('', views.home, name='home'),
    path('create_recipe', views.create_recipe, name='create_recipe'),
    path('signup', views.signup, name='signup'),
    path('recipe', RecipeList.as_view(), name='recipe'),
    path('login', views.login, name='login'),  
    
]