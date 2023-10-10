# forms.py
from django import forms
from .models import CustomUser
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser

class SignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['customer_name', 'email', 'password', 'dob', 'address', 'gender']

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password'] 
