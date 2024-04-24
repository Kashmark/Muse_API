from django.db import models
from .medium import Medium  # Import the Medium model if it's defined in a separate file
from django.contrib.auth.models import (
    User,
)  # Import the User model from Django's built-in authentication system


class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_medium = models.ForeignKey(Medium, on_delete=models.CASCADE)
    bio = models.TextField()
