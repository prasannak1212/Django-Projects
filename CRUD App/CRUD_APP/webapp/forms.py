from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import TextInput, PasswordInput

from .models import Record

# Regiter or create a user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': TextInput(attrs = {'class':"my_fields",
                                           'placeholder': 'Enter your Name',
                                           }), 
            'password1': PasswordInput(attrs = {'class':"my_fields",
                                                'placeholder':'Enter your password',
                                            }), 
            'password2': PasswordInput(attrs = {'class':"my_fields"}),
        }
        

# Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

class CreateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name','last_name','phone','email','address','city','province','country']

class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['first_name','last_name','phone','email','address','city','province','country']