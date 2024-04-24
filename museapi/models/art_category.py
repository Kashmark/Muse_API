# In your_app/models/art_category.py

from django.db import models
from .artwork import Artwork  # Import the Artwork model
from .category import Category  # Import the Category model


class ArtCategory(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
