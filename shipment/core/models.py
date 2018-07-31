from django.db import models
from datetime import datetime, timedelta

class Shipment(models.Model):
    """
    This class represents a shipment, with simple data for informational
    purposes.
    """
    STATUS_CHOICES = (
        ("ORIGIN", "At Origin"),
        ("ENROUTE", "Enroute"),
        ("DESTINATION", "At Destination"),
        ("REFUSED", "Refused Delivery"),
        ("DELIVERED", "Delivered"),
        ("CANCELED", "Canceled Shipment"),
        ("LATE", "Late"))

    status = models.CharField(max_length=30, choices=STATUS_CHOICES,
                              default="ORIGIN")
    sender = models.CharField(max_length=30)
    recipient = models.CharField(max_length=30)
    carrier = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expected_ship_date = models.DateTimeField(default=datetime.now() + timedelta(days=3))
    origin = models.CharField(max_length=40)
    origin_address = models.CharField(max_length=100)
    destination = models.CharField(max_length=40)
    destination_address = models.CharField(max_length=100)
    total_weight = models.CharField(max_length=6)
    total_volume = models.CharField(max_length=6)
