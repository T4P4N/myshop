from django import forms
from .models import Order
from localflavor.in_.forms import *
class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        postal_code = INZipCodeField()
        city = INStateField(required=True)
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city', 'phone_no']

