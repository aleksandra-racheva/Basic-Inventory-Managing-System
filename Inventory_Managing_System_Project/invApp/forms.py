from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {'product_id': 'Product ID', 
                  'name': 'Product Name',
                  'sku': 'Stock Keeping Unit',
                  'price': 'Price',
                  'quantity': 'Quantity',
                  'supplier': 'Supplier',}
        widgets = {
            'product_id': forms.TextInput(attrs={'placeholder':'e.g 1', 'class':'form-control'}),
            'name': forms.TextInput(attrs={'placeholder':'e.g Shirts', 'class':'form-control'}),
            'sku': forms.TextInput(attrs={'placeholder':'e.g S123456', 'class':'form-control'}),
            'price': forms.TextInput(attrs={'placeholder':'e.g 15.75', 'class':'form-control'}),
            'quantity': forms.NumberInput(attrs={'placeholder':'e.g 1', 'class':'form-control'}),
            'supplier': forms.TextInput(attrs={'placeholder':'e.g ABC Corp', 'class':'form-control'}),
        }