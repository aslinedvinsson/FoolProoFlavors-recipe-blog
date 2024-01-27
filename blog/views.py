from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import RecipePost


class RecipePostList(generic.ListView):
    queryset = RecipePost.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

def recipepost_detail(request, slug):
    """
    Display an individual :model:`blog.Recipepost`.

    **Context**

    ``recipepost``
        An instance of :model:`blog.RecipePost`.

    **Template:**

    :template:`blog/recipepost_detail.html`
    """

    queryset = RecipePost.objects.filter(status=1)
    recipepost = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/recipepost_detail.html",
        {"recipepost": recipepost,},
    )