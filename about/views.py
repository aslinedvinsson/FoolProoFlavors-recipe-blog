from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import ContactForm


def about_us(request):
    """
    Displays the "About Us" page with the latest section content and a contact
    form.

    Handles POST requests to save new contact messages, showing a success
    notification upon submission. For GET requests, loads the most recent
    'About' content and a blank contact form.

    Template:
     'about/about.html' and passes 'about' and 'contact_form' as context
     to the template.

    Parameters:
    - request: HttpRequest object.

    Returns:
    - Rendered 'About Us' page with context data.
    """
    if request.method =='POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request,
            messages.SUCCESS, "Contact request received! We endeavour to respond within 2 working days.")
    about = About.objects.all().order_by('-updated_on').first()
    contact_form = ContactForm()
    return render(
        request,
        "about/about.html",
        {"about": about,
        "contact_form": contact_form,
        },
)

