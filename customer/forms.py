from django import forms
from .models import *


class MenuItemForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = '__all__'
        labels = {
            'name': 'Name',
            'description': 'Description',
            'image': 'Image',
            'price': 'Price',
            'category': 'Category'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
            'name': 'Name'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        labels = {
            'user': 'User',
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone'
        }
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'})
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        labels = {
            'customer': 'Customer',
            'complete': 'Complete',
            'transaction_id': 'Transaction Id',
            'is_shipped': 'Is Shipped'
        }
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'complete': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'transaction_id': forms.TextInput(attrs={'class': 'form-control'}),
            'is_shipped': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }


class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = '__all__'
        labels = {
            'menu_item': 'Menu Item',
            'order': 'Order',
            'quantity': 'Quantity'
        }
        widgets = {
            'menu_item': forms.Select(attrs={'class': 'form-control'}),
            'order': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'})
        }


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = '__all__'
        labels = {
            'customer': 'Customer',
            'order': 'Order',
            'address': 'Address',
            'city': 'City'
        }
        widgets = {
            'customer': forms.Select(attrs={'class': 'form-control'}),
            'order': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'})
        }