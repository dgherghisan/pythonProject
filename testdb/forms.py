from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "name",
        "id": "name"
    }))
    price = forms.IntegerField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "price",
        "id": "price"
    }))
    image = forms.FileField(widget=forms.FileInput())

    class Meta:
        model = Product
        fields = [
            'name', 'price', 'image'
        ]
