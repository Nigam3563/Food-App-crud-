from django import forms
from .models import Item
from django.forms import fields


class ItemForm(forms.ModelForm):
    # item_price = forms.IntegerField(max_value=50000)
    # def clean_item_price(self):
    #         item_price = self.cleaned_data.get('item_price')
    #         if item_price<=0:
    #             raise forms.ValidationError("item price shoud be greater then 0")
    #         return item_price

    # def clean(self):
    #     data=super().clean()
    #     item_name = data.get('item')
    #     item_des = data.get('item_des')
    #     if item_name==item_des:
    #         raise forms.ValidationError("must not have same name and description")
    #     return data
    
    class Meta:
        model = Item
        fields =['item_name','item_des', 'item_price','item_image']

        