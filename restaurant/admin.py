# Register your models here.
from django.contrib import admin

from .models import Reservation, Table, Dish, Order, Payment, Customer


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone')
    search_fields = ('name', 'email')


class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'capacity', 'available')
    list_filter = ('available',)


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'table', 'reservation_date', 'status')
    list_filter = ('status', 'reservation_date')
    search_fields = ('customer__name', 'table__number')


class DishAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    search_fields = ('name', 'category')
    list_filter = ('category',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'total_price', 'status')
    list_filter = ('status',)
    search_fields = ('customer__name', 'id')


class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'total_price', 'payment_method')
    list_filter = ('payment_method',)
    search_fields = ('order__id',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'dish', 'rating', 'comment')
    list_filter = ('rating',)
    search_fields = ('user__name', 'dish__name')


admin.site.register(Dish, DishAdmin)
admin.site.register(Table, TableAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Customer, CustomerAdmin)
