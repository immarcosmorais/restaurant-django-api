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
        self.assertEquals(self.customer.name, "Customer created for testing")
        self.assertEquals(self.customer.email, "customer@email.com")
        self.assertEquals(self.customer.phone, "(11) 91111-1111")


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
        self.assertEquals(self.table.number, 1)
        self.assertEquals(self.table.capacity, 4)
        self.assertEquals(self.table.available, True)


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
        self.assertEquals(self.reservation.customer, self.customer)
        self.assertEquals(self.reservation.table, self.table)
        self.assertEquals(self.reservation.status, "confirmed")

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
        self.assertEquals(self.dish.name, "Dish created for testing")
        self.assertEquals(self.dish.description, "Description of the dish created for testing")
        self.assertEquals(self.dish.price, 19.90)
        self.assertEquals(self.dish.category, "Category of the dish created for testing")

class ModelOrderTestCase(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            name="Customer created for testing",
            email="customer@email.com",
            phone="(11) 91111-1111"
        )
        self.order = Order.objects.create(
            customer=self.customer,
            total_price = 59.70,
            status="confirmed"
        )

    def test_to_check_order_attributes(self):
        """
        Test to check attributes of order's model
        """
        self.assertEquals(self.order.customer, self.customer)
        self.assertEquals(self.order.total_price, 59.70)
        self.assertEquals(self.order.status, "confirmed")

class ModelPaymentTestCase(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            name="Customer created for testing",
            email="customer@email.com",
            phone="(11) 91111-1111"
        )
        self.order = Order.objects.create(
            customer=self.customer,
            total_price=59.70,
            status="confirmed"
        )
        self.payment = Payment.objects.create(
            order=self.order,
            customer=self.customer,
            total_price=59.70,
            discount=0,
            payment_method="credit_card"
        )

    def test_to_check_payment_attributes(self):
        """
        Test to check attributes of payment's model
        """
        self.assertEquals(self.payment.order, self.order)
        self.assertEquals(self.payment.customer, self.customer)
        self.assertEquals(self.payment.total_price, 59.70)
        self.assertEquals(self.payment.discount, 0)
        self.assertEquals(self.payment.payment_method, "credit_card")

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
        self.assertEquals(self.review.customer, self.customer)
        self.assertEquals(self.review.dish, self.dish)
        self.assertEquals(self.review.rating, 5)
        self.assertEquals(self.review.comment, "This is a comment for testing")