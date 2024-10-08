from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserRegistrationForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = [
            "username",
            "email",
            "first_name",
            "second_name",
            "password1",
            "password2",
            "role",
            "office",
            "image",
        ]

        labels = {
            "image": "Profile Picture: If you don't upload an image the default image will be used"
        }


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = [
            "first_name",
            "second_name",
            "bio",
            "role",
            "office",
            "image",
        ]
        labels = {"image": "Profile Picture"}
