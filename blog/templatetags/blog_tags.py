from django import template
from django.db.models import Avg
from blog.models import RecipeRating

register = template.Library()


@register.simple_tag
def get_average_rating(recipepost):
    return RecipeRating.objects.filter(recipepost=recipepost).aggregate(
        Avg('reciperating'))['reciperating__avg'] or 0
