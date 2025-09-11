from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from restaurant.views import DishViewSet, OrderViewSet, PaymentViewSet, ReservationViewSet, TableViewSet, \
    CustomerViewSet, ReviewViewSet, ListOrdersByCustomerView, ListPaymentsByCustomerIdView

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Restaurant management API",
      # terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="marcosmorais.contact@gmail.com"),
      # license=openapi.License(name="BSD License"),
   ),
   public=True
   # permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet, basename='Customers')
router.register(r'tables', TableViewSet, basename='Tables')
router.register(r'reservations', ReservationViewSet, basename='Reservations')
router.register(r'dishes', DishViewSet, basename='Dishes')
router.register(r'orders', OrderViewSet, basename='Orders')
router.register(r'payments', PaymentViewSet, basename='Payments')
router.register('reviews', ReviewViewSet, basename='Reviews')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
    path("customers/<int:customer_id>/orders/", ListOrdersByCustomerView.as_view()),
    path("customers/<int:customer_id>/payments/", ListPaymentsByCustomerIdView.as_view()),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
