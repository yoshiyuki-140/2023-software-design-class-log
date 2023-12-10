from django import forms
from myapp.models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'price', 'quantity')
