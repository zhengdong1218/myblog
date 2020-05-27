from django import forms
from django.contrib.auth.models import User

class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

class UserRegisterForm(forms.ModelForm):
    password=forms.CharField()
    password2=forms.CharField()

    class Meta:
        model=User
        fields={'username','email'}

