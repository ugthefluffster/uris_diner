from django import forms
from main.models import *

class ItemAmountForm(forms.Form):
    amount = forms.IntegerField(max_value=99, min_value=1, initial=1)