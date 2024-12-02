from django.contrib import admin
from .models import Category, Customer, Product, Order, Product_variation, Profile
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Product_variation)
admin.site.register(Order)
admin.site.register(Profile)


# mix profile & user info
class ProfileInLine(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username", "first_name", "first_name", "email"]
    inlines = [ProfileInLine]


# unrigester the old way
admin.site.unregister(User)

# Re-Register the new way
admin.site.register(User, UserAdmin)
