# Inspired by the CodeInstitute Walkthrough 'I think, therefor I blog'
from django import forms
from .models import ContactRequest

class ContactForm(forms.ModelForm):
    """
    Form class for creating a ContactRequest instance.

    Utilizes the ContactRequest model and specifies the 'name', 'email',
    and 'message' fields for inclusion in the form.
    """
    class Meta:
        model = ContactRequest
        fields = ('name', 'email', 'message',)
