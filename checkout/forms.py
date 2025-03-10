from django import forms

Quantity = [(i, str(i)) for i in range(1, 10)]
class CartForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=Quantity, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    