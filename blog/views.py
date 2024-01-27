from django.shortcuts import render
from django.views import generic
from .models import RecipePost


class RecipePostList(generic.ListView):
    queryset = RecipePost.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

