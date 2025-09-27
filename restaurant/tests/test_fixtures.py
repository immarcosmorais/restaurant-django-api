from django.test import TestCase
from restaurant.models import Customer, Dish, Review

class FixturesTestCase(TestCase):

    fixtures = ['data_prototype.json']

    def test_fixtures_loaded(self):
        """
        Test to ensure that the fixtures are loaded correctly.
        """
        customer = Customer.objects.get(id=1)
        dishes_count = Dish.objects.get(id=1)
        self.assertEqual(customer.name, "Marcelo Cassiano")
        self.assertEqual(dishes_count.name, "Lasanha Bolonhesa")
