# In your_app/models/order.py

from django.db import models
from django.contrib.auth.models import (
    User,
)  # Import the User model from Django's built-in authentication system
from .payment_type import (
    PaymentType,
)  # Import the PaymentType model if it's defined in a separate file


class Order(models.Model):
    payment_type = models.ForeignKey(
        PaymentType, on_delete=models.PROTECT
    )  # Assuming PROTECT for reference integrity
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
