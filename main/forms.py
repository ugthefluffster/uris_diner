from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.core.validators import *
from main.models import *

class CustomAuthenticationForm(AuthenticationForm):
    template_name = "forms/CustomAuthenticationForm.html"

class CustomUserCreationForm(UserCreationForm):
    template_name = "forms/CustomUserCreationForm.html"
    first_name = forms.CharField(label="First name", max_length=150, required=True)
    last_name = forms.CharField(label="Last name", max_length=150, required=True)
    email = forms.EmailField(label="Email address", required=True)
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields +("email", "first_name", "last_name")

class ChangeInfoForm(forms.ModelForm):
    template_name = "forms/ChangeInfoForm.html"
    first_name = forms.CharField(label="First name", max_length=150, required=True)
    last_name = forms.CharField(label="Last name", max_length=150, required=True)
    email = forms.EmailField(label="Email address", required=True)
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

class CustomPasswordChangeForm(PasswordChangeForm):
  template_name = "forms/CustomPasswordChangeForm.html"

class OrderForm(ModelForm):
    template_name = "forms/OrderForm.html"
    class Meta:
        model = Delivery
        fields = ['address', 'comment']
        widgets = {'comment': forms.Textarea(attrs={'class':'materialize-textarea'})}

class DishForm(ModelForm):
    template_name = "forms/DishForm.html"
    class Meta:
        model = Dish
        fields = ['name', 'price', 'description', 'is_gluten_free', 'is_vegeterian', 'category', 'image_file', 'image_Url']
        labels = {
            'is_gluten_free': 'Gluten free',
            'is_vegeterian': 'Vegeterian',
            'image_file': 'Upload image file',
            'image_Url': 'Enter image URL'
        }
        help_texts = {
            'image_Url': 'Image upload is preferred and will take precedence if both an image URL and a file is supplied.'
        }
        widgets = {
            'description': forms.Textarea(attrs={'class':'materialize-textarea'}),
            'image_file': forms.FileInput(),
        }

class CategoryForm(ModelForm):
    template_name = "forms/CategoryForm.html"
    class Meta:
        model = Category
        fields = ['name', 'image_file', 'image_Url']
        labels = {
            'image_file': 'Upload image file',
            'image_Url': 'Enter image URL'
        }
        help_texts = {
            'image_Url': 'Image upload is preferred and will take precedence if both an image URL and a file is supplied.'
        }
        widgets = {
            'image_file': forms.FileInput(),
        }

class ItemAmountForm(forms.Form):
    amount = forms.IntegerField(max_value=99, min_value=1, initial=1)