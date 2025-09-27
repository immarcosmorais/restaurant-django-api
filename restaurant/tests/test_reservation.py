from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from restaurant.models import Reservation, Customer, Table
from rest_framework import status


class ReservationsTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="admin",
            password="admin123",
        )
        self.url = reverse("Reservations-list")
        self.client.force_authenticate(self.user)
        self.customer_001 = Customer.objects.create(
            name="Customer 001 created for testing",
            email="customer001@email.com",
            phone="(11) 91111-1111"
        )
        self.table_001 = Table.objects.create(
            number=1,
            capacity=4,
            available=True
        )

        self.reservation_001 = Reservation.objects.create(
            customer=self.customer_001,
            table=self.table_001,
            status="confirmed"
        )

        self.customer_002 = Customer.objects.create(
            name="Customer 003 created for testing",
            email="customer002@email.com",
            phone="(11) 91111-1112"
        )

        self.table_002 = Table.objects.create(
            number=2,
            capacity=4,
            available=True
        )

        self.reservation_002 = Reservation.objects.create(
            customer=self.customer_002,
            table=self.table_002,
            status="confirmed"
        )

        self.table_003 = Table.objects.create(
            number=3,
            capacity=4,
            available=True
        )

    def test_list_tables(self):
        """
        Test listing all Tables
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_table(self):
        """
        Test retrieving a specific Table by ID
        """
        response = self.client.get(reverse("Reservations-detail", args=[self.reservation_001.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["customer"], self.reservation_001.customer.id)
        self.assertEqual(response.data["table"], self.reservation_001.table.id)
        self.assertEqual(response.data["status"], self.reservation_001.status)

    def test_create_table(self):
        """
        Test creating a new Table
        """
        data = {
            "customer": self.customer_001.id,
            "table": self.table_003.id,
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["customer"], data["customer"])
        self.assertEqual(response.data["table"], data["table"])

    def test_update_table(self):
        """
        Test updating an existing Table
        """
        data = {
            "customer": self.customer_002.id,
            "table": self.table_003.id,
            "status": "finished"
        }
        response = self.client.put(reverse("Reservations-detail", args=[self.reservation_001.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["customer"], data["customer"])
        self.assertEqual(response.data["table"], data["table"])
        self.assertEqual(response.data["status"], data["status"])

    def test_delete_table(self):
        """
        Test deleting a Table
        """
        response = self.client.delete(reverse("Reservations-detail", args=[self.reservation_002.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)