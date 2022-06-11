from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('recipe', views.recipe, name='recipe'),
    path('create_recipe', views.create_recipe, name='create_recipe'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),  
]