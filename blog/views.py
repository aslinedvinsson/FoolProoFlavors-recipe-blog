from django.shortcuts import render
from django.views import generic
from .models import RecipePost


class RecipePostList(generic.ListView):
    queryset = RecipePost.objects.all()
    template_name = "recipe post_list.html"

