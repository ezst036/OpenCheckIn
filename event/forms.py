from django import forms
from event.models import Event
from account.models import Account

class EventForm(forms.ModelForm):
    name = forms.CharField(max_length=60)
    description = forms.CharField(max_length=100)
    price = forms.IntegerField()
    
    class Meta:
        model = Event
        fields = ['name', 'description', 'price']

class AccountVerificationForm(forms.ModelForm):
    email = forms.EmailField( max_length=60)
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=20)
    address = forms.CharField(max_length=255)
    city = forms.CharField(max_length=60)
    state = forms.CharField(max_length=60)

    class Meta:
        model = Account
        fields = ("email", "first_name", "last_name", "phone_number", "address", "city", "state")
