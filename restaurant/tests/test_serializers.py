from django.test import TestCase
from restaurant.models import Customer, Table, Reservation, Dish, Order, Payment, Review
from restaurant.serializers import CustomerSerializer, TableSerializer, ReservationSerializer, DishSerializer, OrderSerializer, PaymentSerializer, ReviewSerializer

class SerializerCustomerTestCase(TestCase):

    def setUp(self):
        self.customer = Customer.objects.create(
            name = "Customer created for testing",
            email = "customer@email.com",
            phone = "(11) 91111-1111"
        )
        self.serializer_customer = CustomerSerializer(instance=self.customer)

    def test_to_check_fields_of_customer_serializer(self):
        """
        Test to check serialized fields of customer's serializer
        """
        data = self.serializer_customer.data
        self.assertEqual(set(data.keys()), {"id", "name", "email", "phone", "created_at", "updated_at"})

    def test_to_check_content_of_fields_of_customer_serializer(self):
        """
        Test to check content of serialized fields of customer's serializer
        """
        data = self.serializer_customer.data
        self.assertEqual(data["name"], self.customer.name)
        self.assertEqual(data["email"], self.customer.email)
        self.assertEqual(data["phone"], self.customer.phone)


class SerializerTableTestCase(TestCase):
    def setUp(self):
        self.table = Table.objects.create(
            number = 1,
            capacity = 4,
            available = True
        )
        self.serializer_table = TableSerializer(instance=self.table)

    def test_to_check_fields_of_table_serializer(self):
        """
        Test to check serialized fields of table's serializer
        """
        data = self.serializer_table.data
        self.assertEqual(set(data.keys()), {"id", "number", "capacity", "available", "created_at", "updated_at"})

    def test_to_check_content_of_fields_of_table_serializer(self):
        """
        Test to check content of serialized fields of table's serializer
        """
        data = self.serializer_table.data
        self.assertEqual(data["number"], self.table.number)
        self.assertEqual(data["capacity"], self.table.capacity)
        self.assertEqual(data["available"], self.table.available)

class SerializerReservationTestCase(TestCase):
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
        self.serializer_reservation = ReservationSerializer(instance=self.reservation)

    def test_to_check_fields_of_reservation_serializer(self):
        """
        Test to check serialized fields of reservation's serializer
        """
        data = self.serializer_reservation.data
        self.assertEqual(set(data.keys()), {"id", "customer", "table", "reservation_date", "status", "created_at", "updated_at"})

    def test_to_check_content_of_fields_of_reservation_serializer(self):
        """
        Test to check content of serialized fields of reservation's serializer
        """
        data = self.serializer_reservation.data
        self.assertEqual(data["customer"], self.reservation.customer.id)
        self.assertEqual(data["table"], self.reservation.table.id)
        self.assertEqual(data["status"], self.reservation.status)

class SerializerDishTestCase(TestCase):
    def setUp(self):
        self.dish = Dish.objects.create(
            name = "Dish created for testing",
            description = "This is a dish created for testing purposes.",
            price = 19.99,
            category = "Main Course"
        )
        self.serializer_dish = DishSerializer(instance=self.dish)

    def test_to_check_fields_of_dish_serializer(self):
        """
        Test to check serialized fields of dish's serializer
        """
        data = self.serializer_dish.data
        self.assertEqual(set(data.keys()), {"id", "name", "description", "price", "category", "created_at", "updated_at"})

    def test_to_check_content_of_fields_of_dish_serializer(self):
        """
        Test to check content of serialized fields of dish's serializer
        """
        data = self.serializer_dish.data
        self.assertEqual(data["name"], self.dish.name)
        self.assertEqual(data["description"], self.dish.description)
        self.assertEqual(float(data["price"]), float(self.dish.price))
        self.assertEqual(data["category"], self.dish.category)

class SerializerOrderTestCase(TestCase):
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
        self.serializer_order = OrderSerializer(instance=self.order)

    def test_to_check_fields_of_order_serializer(self):
        """
        Test to check serialized fields of order's serializer
        """
        data = self.serializer_order.data
        self.assertEqual(set(data.keys()), {"id", "customer", "total_price", "status", "items", "created_at", "updated_at"})

    def test_to_check_content_of_fields_of_order_serializer(self):
        """
        Test to check content of serialized fields of order's serializer
        """
        data = self.serializer_order.data
        self.assertEqual(data["customer"], self.order.customer.id)
        self.assertEqual(float(data["total_price"]), float(self.order.total_price))
        self.assertEqual(data["status"], self.order.status)
        self.assertEqual(data["items"], [])

class SerializerPaymentTestCase(TestCase):

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
        self.serializer_payment = PaymentSerializer(instance=self.payment)

    def test_to_check_fields_of_payment_serializer(self):
        """
        Test to check serialized fields of payment's serializer
        """
        data = self.serializer_payment.data
        self.assertEqual(set(data.keys()), {"id", "order", "customer", "total_price", "discount", "payment_method", "created_at", "updated_at"})

    def test_to_check_content_of_fields_of_payment_serializer(self):
        """
        Test to check content of serialized fields of payment's serializer
        """
        data = self.serializer_payment.data
        self.assertEqual(data["order"], self.payment.order.id)
        self.assertEqual(data["customer"], self.payment.customer.id)
        self.assertEqual(float(data["total_price"]), float(self.payment.total_price))
        self.assertEqual(float(data["discount"]), float(self.payment.discount))
        self.assertEqual(data["payment_method"], self.payment.payment_method)