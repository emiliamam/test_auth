from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    field_order = ['username', 'lastname', 'email', 'password1', 'password2']