from django.forms import ModelForm
from main.models import *

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image']
