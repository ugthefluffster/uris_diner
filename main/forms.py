from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from main.models import *

class CustomAuthenticationForm(AuthenticationForm):
    # template_name = "form_templates/input_form.html"
    pass

class CustomPasswordChangeForm(PasswordChangeForm):
    template_name = "form_templates/input_form.html"
    
class CustomUserCreationForm(UserCreationForm):
    template_name = "form_templates/input_form.html"
    first_name = forms.CharField(label="First name", max_length=150, required=True)
    last_name = forms.CharField(label="Last name", max_length=150, required=True)
    email = forms.EmailField(label="Email address", required=True)
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields +("email", "first_name", "last_name")

class ChangeInfoForm(forms.ModelForm):
    template_name = "form_templates/input_form.html"
    first_name = forms.CharField(label="First name", max_length=150, required=True)
    last_name = forms.CharField(label="Last name", max_length=150, required=True)
    email = forms.EmailField(label="Email address", required=True)
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

class OrderForm(ModelForm):
    template_name = "form_templates/input_form.html"
    class Meta:
        model = Delivery
        fields = ['address', 'comment']
        widgets = {'comment': forms.Textarea()}

class DishForm(ModelForm):
    template_name = "form_templates/input_form.html"
    class Meta:
        model = Dish
        fields = ['name', 'price', 'description', 'is_gluten_free', 'is_vegeterian', 'category', 'image_file', 'image_Url']
        labels = {
            'is_gluten_free': 'Gluten free',
            'is_vegeterian': 'Vegeterian'
        }
        help_texts = {
            'image_Url': 'Image upload is preferred and will take precedence if both an image URL and a file is supplied.'
        }
        widgets = {
            'category': forms.Select(attrs={'class':'browser-default'}),
            'description': forms.Textarea(attrs={'class':'materialize-textarea'}),
            'image_file': forms.FileInput()
        }

class CategoryForm(ModelForm):
    template_name = "form_templates/input_form.html"
    class Meta:
        model = Category
        fields = ['name', 'image_file', 'image_Url']
        help_texts = {
            'image_Url': 'Image upload is preferred and will take precedence if both an image URL and a file is supplied.'
        }
        widgets = {
            'image_file': forms.FileInput()
        }

class ItemAmountForm(forms.Form):
    template_name = "form_templates/input_form.html"
    amount = forms.IntegerField(max_value=99, min_value=1, initial=1)
