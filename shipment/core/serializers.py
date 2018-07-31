from rest_framework import serializers
from .models import Shipment


class ShipmentSerializer(serializers.ModelSerializer):
    """
    Serializer to map the model instance into JSON format
    """
    class Meta:
        """
        Meta class to map serializer's fields with the model fields.
        """
        model = Shipment
        fields = ("id", "sender", "recipient", "carrier", "created_at",
                  "updated_at", "expected_ship_date", "origin",
                  "origin_address", "destination", "destination_address",
                  "total_weight", "total_volume")
        read_only_fields = ("created_at", "updated_at")
