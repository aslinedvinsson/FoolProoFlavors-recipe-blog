from django.db import models
from django.contrib.auth.models import User
from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

MEAL_TYPES =  ( ("chicken", "Chicken"),
    ("fish", "Fish"),
    ("meat", "Meat"),
    ("vegetarian", "Vegetarian"),
    ("vegan", "Vegan"),
    ("pasta", "Pasta"),
    ("seafood", "Seafood"),
    ("salad", "Salad"),
    ("soup", "Soup"),
    ("sandwich", "Sandwich"),
    ("breakfast", "Breakfast"),
    ("dessert", "Dessert"), )

EFFORT = (("bad_day_comfort_food", "Bad day comfort food"),
("trying_a_healthy_day", "Trying a healthy day"), ("im_in_a_hurry", "I'm in a hurry"),
("i_have_time_but_no_brains", "I have time but no brains"), ("to_far_until_payday", "To far until payday"))

#Inspired by the CodeInstitute Walkthrough 'I think, therefor I blog' and Django Recipe Sharing Tutorial
class RecipePost(models.Model):
    """
    A model to create and manage a recipe post related to :model:`auth.User`
    """

    user = models.ForeignKey(
        User, related_name="blog_posts", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    food_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    ingredients = models.TextField(max_length=10000, null=False, blank=False)
    instructions = models.TextField(max_length=10000, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    meal_type = models.CharField(max_length=50, choices=MEAL_TYPES, default="vegan")
    effort = models.CharField(
        max_length=50, choices=EFFORT, default="Bad day comfort food"
    )
    image_alt = models.CharField(max_length=100, null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(" ", "-")
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f'{self.title} | added by {self.user}'


class Comment(models.Model):
    recipepost = models.ForeignKey(
        RecipePost, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f'Comment {self.body} | added by {self.user}'


class RecipeRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipepost = models.ForeignKey(RecipePost, on_delete=models.CASCADE)
    reciperating = models.IntegerField()

    def __str__(self):
        return f'{self.recipepost.title} | {self.user} - {self.reciperating} out of 10'

