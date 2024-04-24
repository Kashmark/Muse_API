# In your_app/models/order_artwork.py

from django.db import models
from .order import Order  # Import the Order model
from .artwork import Artwork  # Import the Artwork model


class OrderArtwork(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
