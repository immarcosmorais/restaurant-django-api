from decimal import Decimal

from django.test import TestCase
from restaurant.models import Customer, Table, Reservation, Dish, Order, Payment, Review

class ModelCustomerTestCase(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            name = "Customer created for testing",
            email = "customer@email.com",
            phone = "(11) 91111-1111"
        )

    def test_to_check_customer_attributes(self):
        """
        Test to check attributes of customer's model
        """
        self.assertEqual(self.customer.name, "Customer created for testing")
        self.assertEqual(self.customer.email, "customer@email.com")
        self.assertEqual(self.customer.phone, "(11) 91111-1111")


class ModelTableTestCase(TestCase):

    def setUp(self):
        self.table = Table.objects.create(
            number = 1,
            capacity = 4,
            available = True
        )

    def test_to_check_table_attributes(self):
        """
        Test to check attributes of table's model
        """
        self.assertEqual(self.table.number, 1)
        self.assertEqual(self.table.capacity, 4)
        self.assertEqual(self.table.available, True)


class ModelReservationTestCase(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            name="Customer created for testing",
            email="customer@email.com",
            phone="(11) 91111-1111"
        )
        self.table = Table.objects.create(
            number=1,
            capacity=4,
            available=True
        )
        self.reservation = Reservation.objects.create(
            customer=self.customer,
            table=self.table,
            status="confirmed"
        )

    def test_to_check_reservation_attributes(self):
        """
        Test to check attributes of reservation's model
        """
        self.assertEqual(self.reservation.customer, self.customer)
        self.assertEqual(self.reservation.table, self.table)
        self.assertEqual(self.reservation.status, "confirmed")

class ModelDishTestCase(TestCase):

    def setUp(self):
        self.dish = Dish.objects.create(
            name = "Dish created for testing",
            description = "Description of the dish created for testing",
            price = 19.90,
            category = "Category of the dish created for testing"
        )

    def test_to_check_dish_attributes(self):
        """
        Test to check attributes of dish's model
        """
        self.assertEqual(self.dish.name, "Dish created for testing")
        self.assertEqual(self.dish.description, "Description of the dish created for testing")
        self.assertEqual(self.dish.price, 19.90)
        self.assertEqual(self.dish.category, "Category of the dish created for testing")

class ModelOrderTestCase(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            name="Customer created for testing",
            email="customer@email.com",
            phone="(11) 91111-1111"
        )
        self.order = Order.objects.create(
            customer=self.customer,
            total_price = Decimal('59.70'),
            status="confirmed"
        )

    def test_to_check_order_attributes(self):
        """
        Test to check attributes of order's model
        """
        self.assertEqual(self.order.customer, self.customer)
        self.assertEqual(self.order.total_price, Decimal('59.70'))
        self.assertEqual(self.order.status, "confirmed")

class ModelPaymentTestCase(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            name="Customer created for testing",
            email="customer@email.com",
            phone="(11) 91111-1111"
        )
        self.order = Order.objects.create(
            customer=self.customer,
            total_price=Decimal('59.70'),
            status="confirmed"
        )
        self.payment = Payment.objects.create(
            order=self.order,
            customer=self.customer,
            total_price=Decimal('59.70'),
            discount=Decimal('00.00'),
            payment_method="credit_card"
        )

    def test_to_check_payment_attributes(self):
        """
        Test to check attributes of payment's model
        """
        self.assertEqual(self.payment.order, self.order)
        self.assertEqual(self.payment.customer, self.customer)
        self.assertEqual(self.payment.total_price, Decimal('59.70'))
        self.assertEqual(self.payment.discount, Decimal('00.00'))
        self.assertEqual(self.payment.payment_method, "credit_card")

class ModelReviewTestCase(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            name="Customer created for testing",
            email="customer@email.com",
            phone="(11) 91111-1111"
        )
        self.dish = Dish.objects.create(
            name="Dish created for testing",
            description="Description of the dish created for testing",
            price=19.90,
            category="Category of the dish created for testing"
        )
        self.review = Review.objects.create(
            customer=self.customer,
            dish=self.dish,
            rating=5,
            comment="This is a comment for testing"
        )

    def test_to_check_review_attributes(self):
        """
        Test to check attributes of review's model
        """
        self.assertEqual(self.review.customer, self.customer)
        self.assertEqual(self.review.dish, self.dish)
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comment, "This is a comment for testing")