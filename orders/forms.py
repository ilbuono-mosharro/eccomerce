from django import forms
from .models import Order
from localflavor.it.forms import ITProvinceSelect

class OrderCreateForm(forms.ModelForm):
    city = ITProvinceSelect()
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address',
                  'postal_code', 'city']