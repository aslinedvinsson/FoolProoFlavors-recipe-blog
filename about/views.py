from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import ContactForm


def about_us(request):
    """
    Manages "About Us" page: shows content and contact form. On POST, saves
    message and shows success message. On GET, displays 'About' and empty form.
    Uses 'about/about.html' with 'about' and 'contact_form' context.

    Parameters:
    - request: HttpRequest.

    Returns:
    - Rendered page with context.
    """

    if request.method == 'POST':

        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 "Contact request received! We endeavour to"
                                 " respond within 2 working days.")
    about = About.objects.all().order_by('-updated_on').first()
    contact_form = ContactForm()
    return render(
        request,
        "about/about.html", {
                        "about": about,
                        "contact_form": contact_form,
                     },
    )
