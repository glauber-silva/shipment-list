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
        self.shipment_model = mommy.make(Shipment, status="ORIGIN",
                                         sender="Sender X",
                                         recipient="Recipient X",
                                         carrier="Carrier X",
                                         origin="Node 1",
                                         origin_address="Address Origin",
                                         destination="Node 3",
                                         destination_address="Address destination",
                                         total_weight="333",
                                         total_volume="333")

    def test_model_can_create_a_shipment(self):
        """
        Test the shipment model can create a shipment
        """
        self.assertTrue(isinstance(self.shipment_model, Shipment))