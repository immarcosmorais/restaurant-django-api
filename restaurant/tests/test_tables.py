from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from restaurant.models import  Table
from rest_framework import status

class TablesTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="admin",
            password="admin123",
        )
        self.url = reverse("Tables-list")
        self.client.force_authenticate(self.user)

        self.table_001 = Table.objects.create(
            number=1,
            capacity=4,
            available=True
        )

        self.table_002 = Table.objects.create(
            number=2,
            capacity=2,
            available=True
        )

    def test_list_tables(self):
        """
        Test listing all tables
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_table(self):
        """
        Test retrieving a specific table by ID
        """
        response = self.client.get(reverse("Tables-detail", args=[self.table_001.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["number"], self.table_001.number)
        self.assertEqual(response.data["capacity"], self.table_001.capacity)
        self.assertEqual(response.data["available"], self.table_001.available)

    def test_create_table(self):
        """
        Test creating a new table
        """
        data = {
            "number": 3,
            "capacity": 6,
            "available": True
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["number"], data["number"])
        self.assertEqual(response.data["capacity"], data["capacity"])
        self.assertEqual(response.data["available"], data["available"])

    def test_update_table(self):
        """
        Test updating an existing table
        """
        data = {
            "number": 3,
            "capacity": 6,
            "available": False
        }
        response = self.client.put(reverse("Tables-detail", args=[self.table_001.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["number"], data["number"])
        self.assertEqual(response.data["capacity"], data["capacity"])
        self.assertEqual(response.data["available"], data["available"])

    def test_delete_table(self):
        """
        Test deleting a table
        """
        response = self.client.delete(reverse("Tables-detail", args=[self.table_002.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)