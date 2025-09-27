from decimal import Decimal

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from restaurant.models import Customer, Payment, Dish, Order
from rest_framework import status


class PaymentsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username="admin",
            password="admin123",
        )
        self.url = reverse("Payments-list")
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

        self.order_003 = Order.objects.create(
            customer=self.customer_003,
            total_price=59.70,
            status="confirmed"
        )

        self.payment_001 = Payment.objects.create(
            order=self.order_001,
            customer=self.customer_001
            # total_price=self.order_001.total_price,
            # payment_method='cash',
        )

        self.payment_002 = Payment.objects.create(
            order=self.order_002,
            customer=self.customer_002
            # total_price=self.order_002.total_price,
            # payment_method='credit_card',
        )

    def test_list_payments(self):
        """
        Test listing all payments
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_customer(self):
        """
        Test creating a new payment
        """
        data = {
            "order": self.order_003.id,
            "customer": self.customer_003.id,
            "total_price": "59.70",
            "discount": "0.00",
            "payment_method": "debit_card"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["order"], data["order"])
        self.assertEqual(response.data["customer"], data["customer"])
        self.assertEqual(response.data["total_price"], data["total_price"])
        self.assertEqual(response.data["discount"], data["discount"])
        self.assertEqual(response.data["payment_method"], data["payment_method"])

    def test_retrieve_payment(self):
        """
        Test retrieving a specific payment by ID
        """
        response = self.client.get(reverse("Payments-detail", args=[self.payment_001.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["order"], self.payment_001.order.id)
        self.assertEqual(response.data["customer"], self.payment_001.customer.id)
        self.assertEqual(str(response.data["total_price"]), str(self.payment_001.total_price))
        self.assertEqual(str(response.data["discount"]), str(self.payment_001.discount))
        self.assertEqual(response.data["payment_method"], self.payment_001.payment_method)

    def test_update_payment(self):
        """
        Test updating an existing payment
        """
        data = {
            "order": self.order_002.id,
            "customer": self.customer_002.id,
            "total_price": Decimal("59.70"),
            "discount": Decimal("5.00"),
            "payment_method": "debit_card"
        }
        response = self.client.put(reverse("Payments-detail", args=[self.payment_001.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["order"], data["order"])
        self.assertEqual(response.data["customer"], data["customer"])
        self.assertEqual(response.data["total_price"], "54.70")
        self.assertEqual(response.data["discount"], "5.00")
        self.assertEqual(response.data["payment_method"], data["payment_method"])

    def test_delete_payment(self):
        """
        Test deleting a payment
        """
        response = self.client.delete(reverse("Payments-detail", args=[self.payment_002.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)