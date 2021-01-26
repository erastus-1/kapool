from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import AbstractUser
from django import forms
from .models import *

# class RegisterForm(UserCreationForm):
#     email = forms.EmailField()

#     class Meta:
#         model = AbstractUser
#         fields = ['username', 'email', 'contact', 'location', 'password1', 'password2']

# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = AbstractUser
#         fields = ['email', 'location', 'contact']

# class UpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['user', 'bio', 'image', 'contact', 'location'] 