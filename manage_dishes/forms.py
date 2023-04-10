from django.forms import ModelForm
from main.models import *

class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'price', 'description', 'image', 'is_gluten_free', 'is_vegeterian', 'category']
