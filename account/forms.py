from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import HiddenInput
from account.models import Account, Youth, Family

class RegistrationForm(UserCreationForm):
    email = forms.EmailField( max_length=60, help_text='Required.  Add a valid email address')
    username = forms.CharField(max_length=100, help_text='Username required.')

    class Meta:
        model = Account
        fields = ("email", "username", "password1", "password2")

class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    #Hide the image location from user view.  The hidden field is used for deleting previous profile pictures.
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['profileimage'].widget = HiddenInput()
    
    class Meta:
        model = Account
        fields = ['email', 'username', 'first_name', 'middle_name', 'last_name', 'phone_number', 'is_parent', 'profileimage', 'image']
        required_fields = fields

class UploadForm(forms.ModelForm):
    class Meta:
        model = Youth
        fields = ("youth_first_name", "youth_middle_name", "youth_last_name", "image")