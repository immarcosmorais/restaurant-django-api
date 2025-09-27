from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from restaurant.models import Customer
from rest_framework import status


class CustomersTestCase(APITestCase):

    fixtures = ['data_prototype.json']

    def setUp(self):
        self.user = User.objects.get(username="marcos")
        # self.user = User.objects.create_superuser(
        #     username="admin",
        #     password="admin123",
        # )
        self.url = reverse("Customers-list")
        self.client.force_authenticate(self.user)
        # self.customer_001 = Customer.objects.create(
        #     name="Customer One",
        #     email="customer001@exemple.com",
        #     phone="11 91111-1111"
        # )
        # self.customer_002 = Customer.objects.create(
        #     name="Customer Two",
        #     email="customer0012@exemple.com",
        #     phone="11 92222-2222"
        # )

        self.customer_001 = Customer.objects.get(id=1)
        self.customer_002 = Customer.objects.get(id=2)


    def test_list_customers(self):
        """
        Test listing all customers
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_customer(self):
        """
        Test retrieving a specific customer by ID
        """
        response = self.client.get(reverse("Customers-detail", args=[self.customer_001.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.customer_001.name)
        self.assertEqual(response.data["email"], self.customer_001.email)
        self.assertEqual(response.data["phone"], self.customer_001.phone)

    def test_create_customer(self):
        """
        Test creating a new customer
        """
        data = {
            "name": "New Customer",
            "email": "newcustomer@example.com",
            "phone": "11 93333-3333"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], data["name"])
        self.assertEqual(response.data["email"], data["email"])
        self.assertEqual(response.data["phone"], data["phone"])

    def test_update_customer(self):
        """
        Test updating an existing customer
        """
        data = {
            "name": "New Customer",
            "email": "newcustomer@example.com",
            "phone": "11 93333-3333"
        }
        response = self.client.put(reverse("Customers-detail", args=[self.customer_001.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], data["name"])
        self.assertEqual(response.data["email"], data["email"])
        self.assertEqual(response.data["phone"], data["phone"])

    def test_delete_customer(self):
        """
        Test deleting a customer
        """
        response = self.client.delete(reverse("Customers-detail", args=[self.customer_002.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Customer.objects.filter(id=self.customer_002.id).exists())