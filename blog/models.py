from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

MEAL_TYPES = (("chicken", "Chicken"),
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
          ("trying_a_healthy_day", "Trying a healthy day"), ("im_in_a_hurry",
          "I'm in a hurry"), ("i_have_time_but_no_brains",
          "I have time but no brains"),
          ("too_far_until_payday", "Too far until payday"))


# The RecipePost model is a partly customed model through the combination of
# the CodeInstitute Walkthrough 'I think, therefor I blog' and Django
# Recipe Sharing Tutorial
class RecipePost(models.Model):
    """
    A model for recipe posts by users, including fields for ingredients,
    instructions, and images, with automatic slug generation for URLs.

    Methods:
    - save: Overrides the save method to automatically generate a slug from the
    title if one is not provided.

    Meta:
    - ordering: Specifies the default ordering of RecipePost instances by
    creation date in descending order.

    String Representation:
    - Returns a formatted string containing the title of the post and the
    users's username.
    """
    user = models.ForeignKey(
        User, related_name="blog_posts", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    excerpt = models.TextField(blank=True)
    ingredients = models.TextField(max_length=10000, null=False, blank=False)
    instructions = models.TextField(max_length=10000, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    meal_type = models.CharField(max_length=50, choices=MEAL_TYPES,
                                 default="vegan")
    effort = models.CharField(
        max_length=50, choices=EFFORT, default="Bad day comfort food"
    )
    food_image = CloudinaryField('image', default='placeholder')
    image_alt = models.CharField(max_length=100, null=False, blank=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.title.replace(" ", "-")
        super().save(*args, **kwargs)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f'{self.title} | added by {self.user}'


# The comment model is taken from the CodeInstitute Walkthrough
# 'I think, therefor I blog'
class Comment(models.Model):
    """
    A model for comments on RecipePost, including user association, content,
    approval status, and automatic date tracking.

    Meta:
    - ordering: Specifies the default ordering of comments by creation date in
    ascending order.

    String Representation:
    - Returns a formatted string containing the comment body and the username
    of the commenter.
    """
    recipepost = models.ForeignKey(
        RecipePost, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f'Comment {self.body} | added by {self.user}'


# custom model
class RecipeRating(models.Model):
    """
    A model for user ratings on RecipePosts, including the rating value.

    String Representation:
    - Returns a formatted string containing the title of the rated post, the
    username of the rater, and the rating value out of 10.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipepost = models.ForeignKey(RecipePost, on_delete=models.CASCADE)
    reciperating = models.IntegerField()

    def __str__(self):
        title = self.recipepost.title
        user = self.user.user
        rating = self.reciperating
        return f'{title} | {user} - {rating} out of 10'