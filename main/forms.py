from django import forms

class OrderForm(forms.Form):
    address = forms.CharField(max_length=500, required=True)
    comment = forms.CharField(widget=forms.Textarea(), required=False)