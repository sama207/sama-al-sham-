from django.contrib import admin
from .models import ShippingAddress,Order,OrderItem
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)


class OrderItemInLine(admin.StackedInline):
    model=OrderItem
    extra=0

class OrderAdmin(admin.ModelAdmin):
    model=Order
    inlines=[OrderItemInLine]
    fields=["user","order_full_name","shipped","date_shipped"]
    readonly_fields=["date_ordered"]

admin.site.unregister(Order)
admin.site.register(Order,OrderAdmin)



