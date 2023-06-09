from django.db import models
from django.contrib.auth.models import User

def category_image_path(instance, filename):
    return f'categories/{instance.name}.{filename.split(".")[-1]}'

class Category(models.Model):
    name = models.CharField(max_length=20, blank=False, unique=True)
    is_deleted = models.BooleanField(default=False)
    image_Url = models.URLField(null=True, blank=True)
    image_file = models.ImageField(upload_to=category_image_path, null=True, blank=True)
    position = models.IntegerField(blank=False, default=0)

    def __str__(self):
        return self.name

def dish_image_path(instance, filename):
    return f'dishes/{instance.category.name}/{instance.name}.{filename.split(".")[-1]}'

class Dish(models.Model):
    name = models.CharField(max_length=50, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    description = models.CharField(max_length=300, blank=False)
    is_gluten_free = models.BooleanField(default=False)
    is_vegeterian = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, limit_choices_to={'is_deleted':False})
    is_deleted = models.BooleanField(default=False)
    image_Url = models.URLField(null=True, blank=True)
    image_file = models.ImageField(upload_to=dish_image_path, null=True, blank=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return f"{self.id}_{self.user.username}"
    
    @property
    def total_to_pay(self):
        total = sum(item.item_total for item in self.item_set.all())
        return total

class Item(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, blank=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, blank=False)
    amount = models.IntegerField(blank=False, default=1)

    def __str__(self):
        return f"{self.cart} {self.dish.name}({self.amount})"
    
    @property
    def item_total(self):
        total = self.amount * self.dish.price
        return total

class Delivery(models.Model):
    is_delivered = models.BooleanField(default=False)
    address = models.CharField(max_length=200, blank=False)
    comment = models.CharField(max_length=500, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    order = models.OneToOneField(Cart, primary_key=True, on_delete=models.CASCADE)