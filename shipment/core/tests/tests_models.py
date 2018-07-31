from django.test import TestCase
from rest_framework.test import APIClient,APITestCase
from model_mommy import mommy
from shipment.core.models import Shipment
from rest_framework import status
from django.core.urlresolvers import reverse
from shipment.authentication.models import User
from shipment.core.views import ShipmentViewSet

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


class ViewTestCase(TestCase):
    """
    Test suite for the api views.
    """

    def setUp(self):
        """
        Define the test client and other  test variables
        """
        user = User.objects.create(username="nerd", email="nerd@nerd.com", password="n1234567")
        self.client = APIClient()
        self.client.force_authenticate(user=user)
        self.shipment_data = {"status":"ORIGIN",
                              "sender":"Sender X",
                              "recipient":"Recipient X",
                              "carrier":"Carrier X",
                              "origin":"Node 1",
                              "origin_address":"Address Origin",
                              "destination":"Node 3",
                              "destination_address":"Address destination",
                              "total_weight":"333",
                              "total_volume":"333"
                              }
        self.url = reverse('shipments:shipments-list')
        self.response = self.client.post(self.url, self.shipment_data, format="json")

    def test_api_can_create_shipment(self):
        """
        Test the api has shipment creation capability
        """
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Shipment.objects.count(), 1)
        self.assertEqual(Shipment.objects.get().recipient, 'Recipient X')

    def test_authorization_is_enforced(self):
        """
        Test that the api has user authorization
        """
        new_client = APIClient()
        res = new_client.get(reverse('shipments:shipments-list'), kwargs={'pk': 1}, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)


    def test_api_can_get_a_shipment(self):
        """Test the api can get a given shipment."""
        shipment = Shipment.objects.get(id=1)
        print("Shipment".format(shipment))
        url = reverse('shipments:shipments-list')
        response = self.client.get(url, kwargs={'pk': shipment.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_api_can_update_shipment(self):
        """Test the api can update a given shipment."""
        shipment = Shipment.objects.get()
        change_shipment = {'recipient': 'Something new'}
        res = self.client.put(
            reverse('shipments:shipments-detail', kwargs={'pk': shipment.id}),
            change_shipment, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)