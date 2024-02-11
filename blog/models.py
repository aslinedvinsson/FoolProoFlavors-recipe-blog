from django.db import models
from django.contrib.auth.models import User
#from djrichtextfield.models import RichTextField
#from django_resized import ResizedImageField
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

# The RecipePost model is a partly customed model through the combination of
# the CodeInstitute Walkthrough 'I think, therefor I blog' and Django
# Recipe Sharing Tutorial
class RecipePost(models.Model):
    """
    Model for creating and managing recipe posts associated with a User.

    Attributes:
    - user: ForeignKey to the User model, representing the author of the post.
    - title: CharField for the title of the recipe post.
    - slug: SlugField for generating a unique URL slug based on the title.
    - excerpt: TextField for a brief summary or excerpt of the recipe.
    - ingredients: TextField for listing the ingredients of the recipe.
    - instructions: TextField for describing the cooking instructions.
    - created_on: DateTimeField automatically capturing the creation date of
    the post.
    - status: IntegerField representing the status of the post.
    - updated_on: DateTimeField automatically capturing the last update date of
    the post.
    - meal_type: CharField for categorizing the type of meal (e.g., vegan,
    vegetarian).
    - effort: CharField representing the level of effort required to prepare
    the recipe.
    - food_image: CloudinaryField for uploading and storing an image of the
    dish.
    - image_alt: CharField for providing alternative text for the food image.

    Methods:
    - save: Overrides the save method to automatically generate a slug from the
    title if one is not provided.

    Meta:
    - ordering: Specifies the default ordering of RecipePost instances by
    creation date in descending order.

    String Representation:
    - Returns a formatted string containing the title of the post and the
    author's username.
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
    Model for managing comments on RecipePost instances.

    Attributes:
    - recipepost: ForeignKey linking the comment to its associated RecipePost.
    - user: ForeignKey representing the user who posted the comment.
    - body: TextField containing the content of the comment.
    - approved: BooleanField indicating whether the comment has been approved
    for display.
    - created_on: DateTimeField capturing the creation date of the comment.

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
    Model for storing ratings given by users to recipe posts.

    Attributes:
    - user: ForeignKey linking the rating to the user who provided it.
    - recipepost: ForeignKey linking the rating to the RecipePost being rated.
    - reciperating: IntegerField representing the rating value.

    String Representation:
    - Returns a formatted string containing the title of the rated post, the
    username of the rater, and the rating value out of 10.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipepost = models.ForeignKey(RecipePost, on_delete=models.CASCADE)
    reciperating = models.IntegerField()

    def __str__(self):
        return f'{self.recipepost.title} | {self.user.user} - {self.reciperating} out of 10'
