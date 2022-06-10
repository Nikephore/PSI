from django import forms


class VoteAddToBook(forms.Form):
    rate = forms.TypedChoiceField(choices=[(unit, unit) for unit in range(0, 99)], coerce=int)
