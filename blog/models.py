from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

MEAL_TYPES = (("chicken", "Chicken"),("fish", "Fish"), ("meat", "Meat"),
("vegitarian", "Vegitarian"), ("vegan", "Vegan"))

EFFORT = (("bad_day_comfort_food", "Bad day comfort food"),
("trying_a_healthy_day", "Trying a healthy day"), ("im_in_a_hurry", "I'm in a hurry"),
("i_have_time_but_no_brains", "I have time but no brains"))


class RecipePost(models.Model):
    """
    A model to create and manage a recipe post related to :model:`auth.User`
    """

    user = models.ForeignKey(
        User, related_name="blog_posts", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=200, null=False, blank=False)
    slug = models.SlugField(max_length=200, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField(max_length=2000, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    meal_type = models.CharField(max_length=50, choices=MEAL_TYPES, default="fish")
    effort = models.CharField(
        max_length=50, choices=EFFORT, default="Bad day comfort food"
    )
    """
    Need to install django-resized==version?
    v2image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="recipes/",
        force_format="WEBP",
        blank=False,
        null=False,
    )
    """
    image_alt = models.CharField(max_length=100, null=False, blank=False)

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