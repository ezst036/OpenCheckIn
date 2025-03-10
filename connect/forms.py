from django import forms
from . models import ContactConnect

class ConnectForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={}), required=True)
    last_name = forms.CharField(widget=forms.TextInput(attrs={}), required=True)

    class Meta:
        model = ContactConnect
        fields = ['first_name', 'last_name', 'messagetype', 'title', 'body']
        labels = {
            'messagetype': 'Select message: ',
        }