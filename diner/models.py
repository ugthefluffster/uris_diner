from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=200, blank=False, unique=True)
    image = models.CharField(max_length=500)

class Dish(models.Model):
    name = models.CharField(max_length=500, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    description = models.TextField()
    image = models.CharField(max_length=500)
    is_gluten_free = models.BooleanField(default=False)
    is_vegeterian = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

class Item(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, blank=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=False)
    amount = models.IntegerField(blank=False, default=1)

class Delivery(models.Model):
    is_delivered = models.BooleanField(default=False)
    address = models.CharField(max_length=500, blank=False)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    order = models.OneToOneField(Cart, primary_key=True, on_delete=models.CASCADE)