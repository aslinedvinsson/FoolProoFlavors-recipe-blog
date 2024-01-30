from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import RecipePost, Comment

@admin.register(RecipePost)
class RecipePostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'meal_type', 'ingredients', 'user', 'status', 'created_on')
    search_fields = ['title', 'ingredients']
    list_filter = ('status', 'created_on', 'meal_type',)
    prepopulated_fields = {'slug': ('title',)}
    #summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)



