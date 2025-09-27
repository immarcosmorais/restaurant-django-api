from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from restaurant.models import Customer, Dish, Order
from rest_framework import status


class CustomersTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="admin",
            password="admin123",
        )
        self.url = reverse("Orders-list")
        self.client.force_authenticate(self.user)

        self.customer_001 = Customer.objects.create(
            name="Customer One",
            email="customer001@exemple.com",
            phone="11 91111-1111"
        )

        self.customer_002 = Customer.objects.create(
            name="Customer Two",
            email="customer002@exemple.com",
            phone="11 92222-2222"
        )

        self.customer_003 = Customer.objects.create(
            name="Customer Two",
            email="customer003@exemple.com",
            phone="11 93333-3333"
        )

        self.dish_001 = Dish.objects.create(
            name="Dish One",
            description="Description for Dish One",
            price=10.00,
            category="Main Course"
        )
        self.dish_002 = Dish.objects.create(
            name="Dish Two",
            description="Description for Dish Two",
            price=15.00,
            category="Appetizer"
        )

        self.order_001 = Order.objects.create(
            customer=self.customer_001,
            total_price=59.70,
            status="confirmed"
        )

        self.order_002 = Order.objects.create(
            customer=self.customer_002,
            total_price=59.70,
            status="confirmed"
        )

    def test_list_orders(self):
        """
        Test listing all orders
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_order(self):
        """
        Test retrieving a specific order by ID
        """
        responses = self.client.get(reverse("Orders-detail", args=[self.order_001.id]))
        self.assertEqual(responses.status_code, status.HTTP_200_OK)
        self.assertEqual(responses.data["customer"], self.order_001.customer.id)
        self.assertEqual(float(responses.data["total_price"]), float(self.order_001.total_price))
        self.assertEqual(responses.data["status"], self.order_001.status)
        self.assertEqual(responses.data["items"], [])

    def test_create_order(self):
        """
        Test creating a new order
        """
        data = {
            "customer": self.customer_003.id,
            "total_price": 25.00,
            "items": [
                {
                    "dish": self.dish_001.id,
                    "quantity": 1
                },
                {
                    "dish": self.dish_002.id,
                    "quantity": 1
                }
            ]
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["customer"], data["customer"])
        self.assertEqual(float(response.data["total_price"]), float(data["total_price"]))
        self.assertEqual(len(response.data["items"]), 2)

    def test_update_order(self):
        """
        Test updating an existing order
        """
        data = {
            "customer": self.customer_003.id,
            "items": [
                {
                    "dish": self.dish_001.id,
                    "quantity": 1
                },
                {
                    "dish": self.dish_002.id,
                    "quantity": 1
                }
            ]
        }
        response = self.client.put(reverse("Orders-detail", args=[self.order_001.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["customer"], data["customer"])
        # self.assertEqual(float(response.data["total_price"]), float(data["total_price"]))
        self.assertEqual(len(response.data["items"]), 2)

    def test_delete_order(self):
        """
        Test deleting an order
        """
        response = self.client.delete(reverse("Orders-detail", args=[self.order_002.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Order.objects.filter(id=self.order_002.id).exists())