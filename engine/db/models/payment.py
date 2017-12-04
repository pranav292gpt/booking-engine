from django.db import models
from Timestampedmodel import Timestampedmodel
from db.models import Booking

# Payment model to handle payments
class Payment(Timestampedmodel):
    PAYMENT_STATUS_CHOICES = (
            (1, "Pending"),
            (2, "Under Progress"),
            (3, "Failed"),
            (4, "Complete")
            )
    booking = models.OneToOneField(Booking)
    total_amount = models.IntegerField()
    booking_charges = models.IntegerField()
    security_amount = models.IntegerField()
    status = models.IntegerField(choices=PAYMENT_STATUS_CHOICES)
