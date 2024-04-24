# In your_app/models/payment_type.py

from django.db import models
from django.contrib.auth.models import (
    User,
)  # Import the User model from Django's built-in authentication system


class PaymentType(models.Model):
    merchant_name = models.CharField(max_length=100)
    number = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
