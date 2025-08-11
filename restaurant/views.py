from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .models import Customer, Table, Reservation, Dish, Order, Payment, Review
from .serializers import CustomerSerializer, TableSerializer, ReservationSerializer, DishSerializer, OrderSerializer, \
    PaymentSerializer, ReviewSerializer, ListOrdersByCustomerIdSerializer, ListPaymentsByCustomerIdSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'email', 'phone', 'created_at', 'updated_at']
    search_fields = ['name', 'email', 'phone', 'created_at', 'updated_at']
    ordering_fields = ['name', 'email', 'phone', 'created_at', 'updated_at']


class TableViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Table.objects.all()
    serializer_class = TableSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['number', 'capacity', 'available', 'created_at', 'updated_at']
    search_fields = ['number', 'capacity', 'available', 'created_at', 'updated_at']
    ordering_fields = ['number', 'capacity', 'available', 'created_at', 'updated_at']


class ReservationViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['customer__name', 'table__number', 'status', 'reservation_date', 'created_at', 'updated_at']
    search_fields = ['customer__name', 'table__number', 'status', 'reservation_date', 'created_at', 'updated_at']
    ordering_fields = ['customer__name', 'table__number', 'status', 'reservation_date', 'created_at', 'updated_at']


class DishViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'description', 'price', 'category', 'created_at', 'updated_at']
    search_fields = ['name', 'description', 'price', 'category', 'created_at', 'updated_at']
    ordering_fields = ['name', 'description', 'price', 'category', 'created_at', 'updated_at']


class OrderViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['customer__name', 'total_price', 'status', 'created_at', 'updated_at']
    search_fields = ['customer__name', 'total_price', 'status', 'created_at', 'updated_at']
    ordering_fields = ['customer__name', 'total_price', 'status', 'created_at', 'updated_at']


class PaymentViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['customer__name', 'amount', 'payment_date', 'status']


class ReviewViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['order__id', 'customer', 'rating', 'created_at']
    search_fields = ['order__id', 'customer__name', 'rating', 'created_at']
    ordering_fields = ['order__id', 'customer__name', 'rating', 'created_at']


class ListOrdersByCustomerView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ListOrdersByCustomerIdSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return Order.objects.filter(customer__id=customer_id)


class ListPaymentsByCustomerIdView(generics.ListAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ListPaymentsByCustomerIdSerializer

    def get_queryset(self):
        customer_id = self.kwargs['customer_id']
        return Payment.objects.filter(customer__id=customer_id)
