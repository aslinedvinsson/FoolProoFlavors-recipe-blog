# Code taken from the CodeInstitute Walkthrough 'I think, therefor I blog'
# and slightly moified
from django.db import models
from cloudinary.models import CloudinaryField

class About(models.Model):
    """
    Model for storing 'About Us' section details of a website.

    Fields:
    - title: Title of the section.
    - content: Detailed description or content.
    - updated_on: Auto-updated timestamp of the last modification.
    - about_image: CloudinaryField for storing an associated image, with a
    default placeholder.

    The string representation returns the section's title.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    about_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return f'{self.title}'

class ContactRequest(models.Model):
    """
    Model for handling contact form requests.

    Fields:
    - name: Sender's name.
    - email: Sender's email address.
    - message: Contact message content.
    - read: Boolean indicating if the message has been read, defaulting to False.

    The string representation includes the sender's name, indicating the
    origin of the contact request.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Message through contact form request from {self.name}"