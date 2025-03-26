from rest_framework import serializers

from .models import Customer, Table, Reservation, Dish, Order, Payment, OrderItem, Review


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = "__all__"


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        exclude = ["id", 'order']


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, source='order_items')

    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):
        items = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        for item in items:
            OrderItem.objects.create(order=order, **item)
        return order


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"


class ListOrdersByCustomerIdSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, source='order_items')

    class Meta:
        model = Order
        fields = "__all__"


class ListPaymentsByCustomerIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
