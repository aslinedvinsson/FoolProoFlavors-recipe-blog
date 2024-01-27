from django.contrib import admin
from .models import RecipePost, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(RecipePost)
class RecipePostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'user', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# Register your models here.
admin.site.register(Comment)


