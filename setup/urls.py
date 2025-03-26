from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from restaurant.views import MenuViewSet, OrderViewSet, PaymentViewSet, ReservationViewSet, TableViewSet, \
    CustomerViewSet, ReviewViewSet, ListOrdersByCustomerView, ListPaymentsByCustomerIdView

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='Customers')
router.register(r'tables', TableViewSet, basename='Tables')
router.register(r'reservations', ReservationViewSet, basename='Reservations')
router.register(r'dishes', MenuViewSet, basename='Dishes')
router.register(r'orders', OrderViewSet, basename='Orders')
router.register(r'payments', PaymentViewSet, basename='Payments')
router.register('reviews', ReviewViewSet, basename='Reviews')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("customers/<int:customer_id>/orders/", ListOrdersByCustomerView.as_view()),
    path("customers/<int:customer_id>/payments/", ListPaymentsByCustomerIdView.as_view()),
]
