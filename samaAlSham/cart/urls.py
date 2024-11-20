from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.cart_summary, name="cart_summary"),
    path("add/", views.add, name="cart_add"),
    path("update/", views.update, name="cart_update"),
    path("delete/", views.delete, name="cart_delete"),
  
]
