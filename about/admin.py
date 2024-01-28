from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of content in admin
    """
    #list_display = ('title', 'updated_on')
    summernote_fields = ('content',)


