from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from model_mommy import mommy
from django.utils.timezone import datetime
from shipment.core.models import Shipment

from shipment.core.models import Shipment


class ModelTestCase(TestCase):
    """
    This class defines the test suit for the shipment
    """

    def setUp(self):
        """
        Define the test client and other variables
        """
        self.status = "ORIGIN"
        self.sender = "Sender X"
        self.recipient = "Recipient X"
        self.carrier = "Carrier X"
        self.origin = "Node 1"
        self.origin_address = "Address Origin"
        self.destination = "Node 3"
        self.destination_address = "Address destination"
        self.total_weight = "333"
        self.total_volume = "333"
        self.shipment = Shipment(
            status=self.status,
            sender=self.sender,
            recipient=self.recipient,
            carrier=self.carrier,
            origin=self.origin,
            origin_address=self.origin_address,
            destination=self.destination,
            destination_address=self.destination_address,
            total_weight=self.total_weight,
            total_volume=self.total_volume
        )

    def test_model_can_create_a_shipment(self):
        """
        Test the shipment model can create a shipment
        """
        old_count = Shipment.objects.count()
        self.shipment.save()
        new_count = Shipment.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """
    Test suite for the api views.
    """

    def setUp(self):
        """
        Define the test client and other test variables.
        """
        self.client = APIClient()
        self.shipment_data = {
            "shipment": {
                "sender" : "Sender Name",
                "recipient" : "Recipient Name",
                "carrier" : "Carrier Name",
                "origin" : "Origin",
                "origin_address" : "Address",
                "destination" : "Destination",
                "destination_address" : "Destination Address",
                "total_weight": "333",
                "total_volume" : "333"
            }
        }
        self.response = self.client.post(reverse('create'), self.shipment_data, format="json")

    def test_api_can_create_a_shipment(self):
        """
        Test the API has shipment creation capability
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
