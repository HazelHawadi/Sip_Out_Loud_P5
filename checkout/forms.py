from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            'full_name', 'email', 'phone_number',
            'street_address1', 'street_address2',
            'town_or_city', 'postcode', 'country',
            'county',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Enter your Full Name',
            'email': 'Enter your Email Address',
            'phone_number': 'Enter your Phone Number',
            'country': 'Select your Country',
            'postcode': 'Enter Postal Code',
            'town_or_city': 'Enter Town or City',
            'street_address1': 'Enter Street Address 1',
            'street_address2': 'Enter Street Address 2 (Optional)',
            'county': 'Enter County/State',
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'form-control stripe-style-input'
            self.fields[field].label = False
