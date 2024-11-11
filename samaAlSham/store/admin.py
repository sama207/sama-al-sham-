from django.contrib import admin
from . models import Category,Customer,Product,Order,Product_variation
# Register your models here.
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Product_variation)
admin.site.register(Order)
