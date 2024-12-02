from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("login/",views.login_user,name='login'),
    path("logout/",views.logout_user,name='logout'),
    path("register/",views.register_user,name='register'),
    path("product/<int:pk>",views.product,name='product'),
    path("category/<str:cat>",views.category,name='category'),
    path("update_user/",views.update_user,name='update_user'),
    path("update_password/",views.update_password,name='update_password'),
    path("update_info/",views.update_info,name='update_info'),
]
