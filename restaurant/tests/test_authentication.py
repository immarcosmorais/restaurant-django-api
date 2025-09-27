from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from django.urls import reverse
from rest_framework import status


class AuthenticationTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="admin",
            password="admin123",
        )
        self.url = reverse("Customers-list")

    def test_authentication_with_valid_credentials(self):
        """
        Test authentication with valid credentials
        """
        user = authenticate(username="admin", password="admin123")
        self.assertIsNotNone(user)
        self.assertTrue(user.is_authenticated)

    def test_authentication_with_invalid_credentials(self):
        """
        Test authentication with invalid credentials
        """
        user = authenticate(username="admin", password="wrongpassword")
        self.assertIsNone(user)
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_access_protected_endpoint_with_authentication(self):
        """
        Test access to a protected endpoint with authentication.
        """
        self.client.force_authenticate(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
