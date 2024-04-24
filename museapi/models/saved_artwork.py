# In your_app/models/saved_artwork.py

from django.db import models
from django.contrib.auth.models import (
    User,
)  # Import the User model from Django's built-in authentication system
from .artwork import Artwork  # Import the Artwork model


class SavedArtwork(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
