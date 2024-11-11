from django.db import models
import datetime


# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=50)
    parent_category_id = models.IntegerField(null=True, blank=True)
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='categories'


class Product(models.Model):
    summ_or_win = {"summer": "صيفي", "winter": "شتوي"}
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250, default="", blank=True, null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    summer_or_winter = models.CharField(max_length=20, choices=summ_or_win, null=True)
    created_at = models.DateField(default=datetime.datetime.today)
    updated_at = models.DateField(default=datetime.datetime.today,blank=True,null=True)
    image = models.ImageField(upload_to="uploads/product/")
    is_on_sale=models.BooleanField(default=False)
    sale_price=models.DecimalField(default=0,decimal_places=2,max_digits=6)

    def __str__(self):
        return self.name


class Product_variation(models.Model):
    product_sizes = {
        "S": "Small",
        "M": "Medium",
        "L": "Large",
        "XL": "Extra Large",
        "2XL": "Extra Extra Large",
        "3XL": "Extra Extra Extra Large",
        "4XL": "Extra Extra Extra Extra Large",
    }
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    size = models.CharField(max_length=10, choices=product_sizes)
    color = models.CharField(max_length=10)
    stock_quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.product}"


class Customer(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name}{self.last_name}"


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True)
    address = models.CharField(max_length=100, default="", blank=True)
    phone = models.CharField(max_length=20, default="", blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product}{self.customer}"
