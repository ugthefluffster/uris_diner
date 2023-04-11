from django import forms
from django.forms import ModelForm
from main.models import *

class OrderForm(ModelForm):
    class Meta:
        model = Delivery
        fields = ['address', 'comment']
        widgets = {
            'comment': forms.Textarea()
        }
