from crispy_forms.helper import FormHelper
from django.forms import ModelForm
from django import forms
from .models import Recipe


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'prep_time', 'cook_time', 
        'serves', 'ingredients', 'instructions', 'featured_image', ]
        def __init__(self, *args, **kwargs):
            super(RecipeForm, self).__init__(*args, **kwargs)
            self.helper = FormHelper()
            self.helper.form_show_labels = False 