from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from restaurant.models import Dish
from rest_framework import status


class CustomersTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="admin",
            password="admin123",
        )
        self.url = reverse("Dishes-list")
        self.client.force_authenticate(self.user)
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
    def test_list_dishes(self):
        """
        Test listing all dishes
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_dish(self):
        """
        Test retrieving a specific dish by ID
        """
        response = self.client.get(reverse("Dishes-detail", args=[self.dish_001.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.dish_001.name)
        self.assertEqual(response.data["description"], self.dish_001.description)
        self.assertEqual(float(response.data["price"]), float(self.dish_001.price))
        self.assertEqual(response.data["category"], self.dish_001.category)

    def test_create_dish(self):
        """
        Test creating a new dish
        """
        data = {
            "name": "New Dish",
            "description": "Description for New Dish",
            "price": 20.00,
            "category": "Dessert"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], data["name"])
        self.assertEqual(response.data["description"], data["description"])
        self.assertEqual(float(response.data["price"]), float(data["price"]))
        self.assertEqual(response.data["category"], data["category"])

    def test_update_dish(self):
        """
        Test updating an existing dish
        """
        data = {
            "name": "Updated Dish",
            "description": "Updated description for Dish One",
            "price": 12.00,
            "category": "Main Course"
        }
        response = self.client.put(reverse("Dishes-detail", args=[self.dish_001.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], data["name"])
        self.assertEqual(response.data["description"], data["description"])
        self.assertEqual(float(response.data["price"]), float(data["price"]))
        self.assertEqual(response.data["category"], data["category"])

    def test_delete_dish(self):
        """
        Test deleting a dish
        """
        response = self.client.delete(reverse("Dishes-detail", args=[self.dish_002.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Dish.objects.filter(id=self.dish_002.id).exists())