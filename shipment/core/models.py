from django.db import models


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

    status = models.CharField(choices=STATUS_CHOICES, default="ORIGIN")
    recipient = models.CharField(max_length=30, blank=False, null=False)
    carrier = models.CharField(max_length=15, blank=False, null=False)
    expected_ship_date = models.DateField(blank=False)
    origin = models.CharField(max_length=40, blank=False, null=False)
    destination = models.CharField(max_length=40, blank=False, null=False)
    total_weight = models.CharField(max_length=6, blank=False, null=False)
    total_volume = models.CharField(max_length=6, blank=False, null=False)
