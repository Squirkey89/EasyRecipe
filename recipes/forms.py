from crispy_forms.helper import FormHelper
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
from .models import Recipe, Comment


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'prep_time', 'cook_time', 
            'serves', 'ingredients', 'instructions', 'featured_image' ]
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

        