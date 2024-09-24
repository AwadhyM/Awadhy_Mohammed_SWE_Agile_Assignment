from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    DetailView,
    DeleteView,
    UpdateView,
)
from .forms import CustomUserRegistrationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserDetailView(DetailView):
    """
    Displays a single profile for view.

    Attributes:
            model : Model
                    The model entity that will be viewed.

            template_name : Str
                    The template that contains html and css code for display of the records.
    """

    model = CustomUser
    template_name = "user_management/profile.html"

    def get_object(self):
        """Gets the user id which is used in the url."""
        user_id = self.kwargs.get("userid")

        try:
            return CustomUser.objects.get(id=user_id)
        except:
            messages.error(self.request, f"User could not be found")
            redirect("/")


class CustomUserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
        View for updating a User account.

    Inherits from:
        LoginRequiredMixin: Ensures that the user is logged in.
        UserPassesTestMixin: Ensures that the user passes a custom test.
        UpdateView: Provides the ability to update an existing object.

    Attributes:
        model : Model
                        The model that this view will act upon.
        fields : list(str)
                        The fields of the model to be displayed in the form.

    """

    model = CustomUser
    template_name = "user_management/profile_modify.html"
    form_class = CustomUserChangeForm
    success_url = "/"

    def form_valid(self, form):
        """Function handles how form is saved"""
        form.instance.author = self.request.user
        messages.success(
            self.request,
            f"User {self.get_object().username} account successfully updated.",
        )
        return super().form_valid(form)

    def test_func(self):
        """Function ensures that only the author of article can edit an article"""
        custom_user = self.get_object()
        if self.request.user == custom_user:
            return True
        else:
            return False

    def get_object(self):
        return self.request.user


class CustomUserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
        View for deleting an existing article.

    Inherits from:
        LoginRequiredMixin: Ensures that the user is logged in.
        UserPassesTestMixin: Ensures that the user passes a custom test.
        DeleteView: Provides the ability to delete an existing object.

    Attributes:
        model : Model
                        The model that this view will act upon.
        success_url : str
                    Where the user is redirected to after completion of delete.

    """

    model = CustomUser
    template_name = "user_management/user_confirm_delete.html"
    success_url = "/"

    def test_func(self):
        """Ensures that user has admin status. As this is a requirement for deletion."""
        return self.request.user.is_superuser

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, "User has been successfully removed")
        return response

    def get_object(self, queryset=None):
        """Hook to ensure object is the user to be deleted, not the requestor"""
        obj = super().get_object(queryset)
        if obj == self.request.user:
            raise Exception("You cannot delete your own account.")
        return obj


@login_required
def user_logout(request):
    """Routes user to logout page"""
    logout(request)
    return render(request, "user_management/logout.html", {})


def register(request):
    """Routes user to registration page where they can register an account"""

    if request.method == "POST":
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request,
                f"Account successfully created for {username}. You can now login using the form below.",
            )
            return redirect("login")
    else:
        form = CustomUserRegistrationForm()

    context = {"form": form}
    return render(request, "user_management/register.html", context)
