# In your_app/models/artwork.py

from django.db import models
from .artist import Artist  # Import the Artist model
from .medium import Medium  # Import the Medium model


class Artwork(models.Model):
    price = models.IntegerField()
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    medium = models.ForeignKey(Medium, on_delete=models.CASCADE)
    picture_url = models.URLField()
    description = models.TextField()
