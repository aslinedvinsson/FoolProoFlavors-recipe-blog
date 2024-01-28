from django.shortcuts import render
from .models import About


def about_us(request):

    """
    Taken from walk trhough: rewrite
    Renders the About page
    **Template**
    :template:`about/about.html`
    """

    about = About.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
)

