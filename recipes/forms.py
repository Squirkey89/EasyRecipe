from crispy_forms.helper import FormHelper
from django.forms import ModelForm
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
from .models import Recipe, Comment


class RecipeForm(ModelForm):
    """
    Form that allows to add recipe
    """
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'prep_time', 'cook_time', 'serves',
                  'ingredients', 'instructions', 'featured_image']

        widgets = {
            'ingredients': SummernoteWidget(),
            'instructions': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)


class CommentForm(forms.ModelForm):
    """
    Form that allows to add comments
    """
    class Meta:
        model = Comment
        fields = ('body',)
