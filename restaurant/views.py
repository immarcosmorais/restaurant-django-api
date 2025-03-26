from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Customer, Table, Reservation, Dish, Order, Payment, Review
from .serializers import CustomerSerializer, TableSerializer, ReservationSerializer, DishSerializer, OrderSerializer, \
    PaymentSerializer, ReviewSerializer, ListOrdersByCustomerIdSerializer, ListPaymentsByCustomerIdSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class TableViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


class MenuViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class OrderViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


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
