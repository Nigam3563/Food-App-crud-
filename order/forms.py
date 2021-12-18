from django import forms
from .models import *
from django.forms import fields

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields ='__all__'

class OrderItemForm(forms.ModelForm):
    # exclude = ('OrderForm')
    class Meta:
        model =OrderItem
        fields ='__all__'
        exclude=('order',)

