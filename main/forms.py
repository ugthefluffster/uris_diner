from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from main.models import *

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label="First name", max_length=150, required=True)
    last_name = forms.CharField(label="Last name", max_length=150, required=True)
    email = forms.EmailField(label="Email address", required=True)
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields +("email", "first_name", "last_name")

class ChangeInfoForm(forms.ModelForm):
    first_name = forms.CharField(label="First name", max_length=150, required=True)
    last_name = forms.CharField(label="Last name", max_length=150, required=True)
    email = forms.EmailField(label="Email address", required=True)
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

class OrderForm(ModelForm):
    class Meta:
        model = Delivery
        fields = ['address', 'comment']
        widgets = {'comment': forms.Textarea()}

class DishForm(ModelForm):
    class Meta:
        model = Dish
        fields = ['name', 'price', 'description', 'is_gluten_free', 'is_vegeterian', 'category', 'image_Url', 'image_file']
        help_texts = {
            'image_Url': 'Image upload is preferred and will take precedence if both an image URL and a file is supplied.'
        }

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'image_Url', 'image_file']
        help_texts = {
            'image_Url': 'Image upload is preferred and will take precedence if both an image URL and a file is supplied.'
        }

class ItemAmountForm(forms.Form):
    amount = forms.IntegerField(max_value=99, min_value=1, initial=1)
