from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import CustomUser


class CustomUserRegistrationForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "first_name",
            "second_name",
            "password1",
            "password2",
            "role",
            "office",
            "image",
        ]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "second_name", "role", "office", "image"]
