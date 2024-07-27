from django import forms
from .models import Customer, Product, OrderItem

class ExistingCustomerForm(forms.Form):
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), required=False, widget=forms.Select(attrs={'class': 'form-control'}))

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
        }

class OrderItemForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']
        widgets = {
            'product': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
        }

class OrderQueryForm(forms.Form):
    order_number = forms.IntegerField(label="Número de Pedido", widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Número de Pedido'}))
