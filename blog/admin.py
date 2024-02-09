# Inspired by the CodeInstitute Walkthrough 'I think, therefor I blog'
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import RecipePost, Comment, RecipeRating

@admin.register(RecipePost)
class RecipePostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'meal_type', 'ingredients', 'user', 'status',
    'created_on')
    search_fields = ['title', 'ingredients']
    list_filter = ('status', 'created_on', 'meal_type',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ('created_on', 'user', 'approved', 'recipepost')
    search_fields = ['user', 'approved']


@admin.register(RecipeRating)
class RecipeRatingAdmin(SummernoteModelAdmin):

    list_display = ('reciperating', 'user', 'recipepost')
    search_fields = ['user', 'reciperating']






