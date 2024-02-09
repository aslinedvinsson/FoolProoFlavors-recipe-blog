# Inspired by the CodeInstitute Walkthrough 'I think, therefor I blog'
from django import forms
from .models import ContactRequest

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ('name', 'email', 'message',)
