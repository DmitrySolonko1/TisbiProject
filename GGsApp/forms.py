from django import forms
from django.forms import ModelChoiceField

from .models import Product, Marketplace, ProductType

class ProductForm(forms.ModelForm):
    marketplace = ModelChoiceField(Marketplace.objects.all(), label='Площадка', empty_label='Выберите значение')
    product_type = ModelChoiceField(ProductType.objects.all(), label='Тип продукта', empty_label='Выберите значение')

    class Meta:
        model = Product
        fields = ['title', 'description', 'image', 'marketplace', 'product_type', 'price', 'client_nickname']
        exclude = ['client_nickname']