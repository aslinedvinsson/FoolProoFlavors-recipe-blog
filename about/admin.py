from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, ContactRequest

# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of content in admin
    """
    #list_display = ('title', 'updated_on')
    summernote_fields = ('content',)


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):

    list_display = ('message', 'read',)




    ####Dubbelkolla sida