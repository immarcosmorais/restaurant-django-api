from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.urls import reverse
from restaurant.models import Customer, Dish, Review
from rest_framework import status

class ReviewsTestCase(APITestCase):

    def setUp(self):

        self.user = User.objects.create_superuser(
            username="admin",
            password="admin123",
        )

        self.url = reverse("Reviews-list")
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
            name="Customer Three",
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

        self.dish_003 = Dish.objects.create(
            name="Dish Three",
            description="Description for Dish Three",
            price=20.00,
            category="Dessert"
        )

        self.review_001 = Review.objects.create(
            customer=self.customer_001,
            dish=self.dish_001,
            rating=5,
            comment="Excellent dish!"
        )

        self.review_002 = Review.objects.create(
            customer=self.customer_002,
            dish=self.dish_002,
            rating=4,
            comment="Very good, but could be improved."
        )

        self.review_003 = Review.objects.create(
            customer=self.customer_003,
            dish=self.dish_003,
            rating=3,
            comment="Average, nothing special."
        )

    def test_list_reviews(self):
        """
        Test listing all reviews
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_review(self):
        """
        Test creating a new review
        """
        data = {
            "customer": self.customer_001.id,
            "dish": self.dish_003.id,
            "rating": 4,
            "comment": "Good dish!"
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["customer"], data["customer"])
        self.assertEqual(response.data["dish"], data["dish"])
        self.assertEqual(response.data["rating"], data["rating"])
        self.assertEqual(response.data["comment"], data["comment"])

    def test_retrieve_review(self):
        """
        Test retrieving a specific review by ID
        """
        response = self.client.get(reverse("Reviews-detail", args=[self.review_001.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["customer"], self.review_001.customer.id)
        self.assertEqual(response.data["dish"], self.review_001.dish.id)
        self.assertEqual(response.data["rating"], self.review_001.rating)
        self.assertEqual(response.data["comment"], self.review_001.comment)

    def test_update_review(self):
        """
        Test updating an existing review
        """
        data = {
            "customer": self.customer_002.id,
            "dish": self.dish_001.id,
            "rating": 2,
            "comment": "Not as good as I expected."
        }
        response = self.client.put(reverse("Reviews-detail", args=[self.review_002.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["customer"], data["customer"])
        self.assertEqual(response.data["dish"], data["dish"])
        self.assertEqual(response.data["rating"], data["rating"])
        self.assertEqual(response.data["comment"], data["comment"])

    def test_delete_review(self):
        """
        Test deleting a review
        """
        response = self.client.delete(reverse("Reviews-detail", args=[self.review_003.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Review.objects.filter(id=self.review_003.id).exists())