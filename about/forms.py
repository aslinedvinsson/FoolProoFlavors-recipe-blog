# Inspired by the CodeInstitute Walkthrough 'I think, therefor I blog'
from django import forms
from .models import ContactRequest


class ContactForm(forms.ModelForm):
    """
    Form class for creating a ContactRequest with 'name', 'email', and
    'message' fields.
    """
    class Meta:
        model = ContactRequest
        fields = ('name', 'email', 'message',)
