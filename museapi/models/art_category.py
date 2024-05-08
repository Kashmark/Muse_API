from django.db import models
from .artwork import Artwork  
from .category import Category  


class ArtCategory(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
