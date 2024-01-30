from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import ContactForm


def about_us(request):

    """
    Renders the most recent information on the website user and allows contact
    request.
    Displays an individual instance of :model:`about.About`.
    **Context**
    ``about```
        The most recent instance of :model:`about.About`.
    ``contact_form``
        An instance of :form: `about.ContactForm`.
    **Template:**
    :template:`about/about.html`
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

