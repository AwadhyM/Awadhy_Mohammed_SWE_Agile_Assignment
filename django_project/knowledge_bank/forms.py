from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    """
    A form for creating new users. Inherits from Django's UserCreationForm.

    This form includes all the standard fields from UserCreationForm, and can be customized
    to include additional fields or validation logic as needed.

    Attributes:
    email
    """

    email = forms.EmailField()

    class Meta:
        """
        Contains metadata for UserRegistrationForm.

        This class can be customised to configure the different sections of the form
        that users will use for account registration.

        Attributes:
        model (User): The model that will be used to create the user.
        fields (list): The fields that will be included in the form.
        """

        model = User
        fields = ["username", "email", "password1", "password2"]
