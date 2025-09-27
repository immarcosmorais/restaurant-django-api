from decimal import Decimal

from django.db import models
from rest_framework.exceptions import ValidationError


class Bean(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Customer(Bean):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13, unique=True)


class Table(Bean):
    number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    available = models.BooleanField(default=True)


class Reservation(Bean):
    STATUS_CHOICES = [
        ("confirmed", "Confirmed"),
        ("cancelled", "Cancelled"),
        ("finished", "Finished")
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE, default=None)
    reservation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="confirmed")

    def save(self, *args, **kwargs):
        if self.status == "confirmed" and self.table.available:
            self.table.available = False
        elif self.status == "cancelled" or self.status == "finished":
            self.table.available = False
        else:
            raise ValidationError(f"Table {self.table.number} with id {self.table.id} is already reserved")

        self.table.save()
        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        if not self.table.available:
            self.table.available = True
            self.table.save()
        super().delete()


class Dish(Bean):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=240, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, db_index=True)


class Order(Bean):
    STATUS_CHOICES = [
        ("confirmed", "Confirmed"),
        ("preparing", "Preparing"),
        ("cancelled", "Cancelled"),
        ("paid", "Paid")
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="confirmed")

    def calculate_total_price(self):
        total = Decimal('0.00')
        for item in self.order_items.all():
            total += item.sub_total_price
        self.total_price = total
        super().save(update_fields=['total_price'])


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sub_total_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))

    def save(self, *args, **kwargs):
        self.sub_total_price = self.dish.price * self.quantity
        super().save(*args, **kwargs)
        self.order.calculate_total_price()


class Payment(Bean):
    PAYMENT_METHODS_CHOICES = [
        ("credit_card", "Credit Card"),
        ("debit_card", "Debit Card"),
        ("cash", "Cash"),
    ]
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal('0.00'))
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHODS_CHOICES, default="cash")

    def save(self, *args, **kwargs):
        if self.order.status != "paid":
            self.order.status = "paid"
        order_total = Decimal(str(self.order.total_price))
        discount = Decimal(str(self.discount))
        self.order.save()
        self.total_price = order_total - discount
        super().save(*args, **kwargs)


class Review(Bean):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    rating = models.IntegerField(default=1, choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True, null=True)
