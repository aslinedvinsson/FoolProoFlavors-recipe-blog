from django.db import models


class About(models.Model):
    """
    A model to create and manage content in an About page
    ********related to :model:`auth.User`
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

