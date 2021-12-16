from django import forms
from django.forms.utils import ErrorList

class CartAddBookForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, required=True)
    
class OrderCreateForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    address = forms.CharField(max_length=300)
    postal_code = forms.CharField(max_length=5)
    city = forms.CharField(max_length=50)
    