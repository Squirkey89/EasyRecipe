from django.contrib import admin
from . models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Add Summernote to Recipe admin
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'recipe')
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description', 'ingredients', 'instructions')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Ability to manage comments in admin
    """
    list_display = ('name', 'body', 'recipe', 'created_on', 'approved')
    list_filter = ('created_on', 'approved')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        Ability to approve comments
        """
        queryset.update(approved=True)
