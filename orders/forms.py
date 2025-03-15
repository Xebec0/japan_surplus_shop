from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    """
    Form for creating a new order
    """
    class Meta:
        model = Order
        fields = ['full_name', 'email', 'phone', 'address', 'city', 'state', 
                  'postal_code', 'country', 'payment_method']
        widgets = {
            'address': forms.Textarea(attrs={'rows': 3}),
            'payment_method': forms.RadioSelect(),
        } 