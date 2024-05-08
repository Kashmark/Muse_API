from django.db import models
from .medium import Medium
from django.contrib.auth.models import (
    User,
)


class Artist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    preferred_medium = models.ForeignKey(Medium, on_delete=models.CASCADE)
    bio = models.TextField()
