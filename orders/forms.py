from django import forms

from orders.models import Order

class CartAddBookForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, required=True)
    
class OrderCreateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    address = forms.CharField(max_length=300)
    postal_code = forms.CharField(max_length=5)
    city = forms.CharField(max_length=50)
       
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address', 'postal_code', 'city',  )