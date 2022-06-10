from django import forms

from catalog.models import Vote

class VoteAddToBook(forms.Form):
    rate = forms.TypedChoiceField(choices=[(unit, unit) for unit in range(0, 99)], coerce=int)