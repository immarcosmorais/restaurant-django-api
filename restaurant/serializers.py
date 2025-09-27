from rest_framework import serializers

from .models import Customer, Table, Reservation, Dish, Order, Payment, OrderItem, Review
from .validators import invalid_phone, invalid_email, invalid_name


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

    def validate(self, attrs):
        if invalid_phone(attrs.get('phone')):
            raise serializers.ValidationError({"phone": "Phone must be a valid phone number with 13 characters."})
        if invalid_email(attrs.get('email')):
            raise serializers.ValidationError({"email": "Email must be a valid email address."})
        if invalid_name(attrs.get('name')):
            raise serializers.ValidationError(
                {"name": "Name must be at least 3 characters long and contain only letters."})
        return attrs


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

    def update(self, instance, validated_data):
        items = validated_data.pop('order_items', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if items is not None:
            instance.order_items.all().delete()
            for item in items:
                OrderItem.objects.create(order=instance, **item)

        return instance


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
