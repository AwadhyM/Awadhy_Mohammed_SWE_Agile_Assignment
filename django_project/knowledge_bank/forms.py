from django import forms
from django.contrib.auth.forms import UserCreationForm
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


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["first_name", "second_name", "role", "office", "image"]
