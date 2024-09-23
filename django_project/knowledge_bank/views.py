from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.views.generic.edit import CreateView
from .forms import CustomUserRegistrationForm, CustomUserChangeForm
from .models import Article, CustomUser


class ArticleListView(ListView):
    """
    Displays a list of articles.

    This view inherits from Django's builtin ListView. It has been
    customised to order articles based on date posted with the most
    recent at the top.

    Attributes:
            model : Model
                    The model entities that will be viewed.

            template_name : Str
                    The template that contains html and css code for display of the records.

            context_object_name : Str
                    The context variable used for list of objects.
    """

    template_name = "knowledge_bank/home.html"
    model = Article
    context_object_name = "articles"
    ordering = ["-date_posted"]


class ArticleDetailView(DetailView):
    """
    Displays a single article for view.

    Attributes:
            model : Model
                    The model entity that will be viewed.
    """

    model = Article


class ArticleCreateView(LoginRequiredMixin, CreateView):
    """
        Displays a single article for view.

    This view requires the user to be logged in to access it.
    It displays a form for creating a new MyModel instance and handles
    the form submission.

    Attributes:
        model : Model
            The model that this view will create an instance of.

        fields : list(str)
            The fields of the model to be displayed in the form.
    """

    model = Article
    fields = ["title", "content"]

    def form_valid(self, form):
        """Function handles how form is saved"""
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
        View for updating an existing article.

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

    model = Article
    fields = ["title", "content"]

    def form_valid(self, form):
        """Function handles how form is saved"""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        """Function ensures that only the author of article can edit an article"""
        article = self.get_object()
        if self.request.user == article.author:
            return True
        else:
            return False


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
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

    model = Article
    success_url = "/"

    def test_func(self):
        """Ensures that user has admin status. As this is a requirement for deletion."""
        return self.request.user.is_superuser


class ProfileDetailView(DetailView):
    """
    Displays a single profile for view.

    Attributes:
            model : Model
                    The model entity that will be viewed.

            template_name : Str
                    The template that contains html and css code for display of the records.
    """

    model = CustomUser
    template_name = "knowledge_bank/profile.html"

    def get_object(self):
        """Gets the user id which is used in the url."""
        user_id = self.kwargs.get("userid")

        try:
            return CustomUser.objects.get(id=user_id)
        except:
            messages.error(self.request, f"User could not be found")
            redirect("/")


@login_required
def profile_modify(request):
    """Routes user to their profile page. If they are logged in."""
    if request.method == "POST":
        user_form = CustomUserChangeForm(
            request.POST, request.FILES, instance=request.user
        )
        if user_form.is_valid():
            user_form.save()
            messages.success(request, f"Account successfully updated.")
            return redirect("profile-modify")
    else:
        user_form = CustomUserChangeForm(instance=request.user)

    context = {"user_form": user_form}

    return render(request, "knowledge_bank/profile_modify.html", context)


@login_required
def user_logout(request):
    """Routes user to logout page"""
    logout(request)
    return render(request, "knowledge_bank/logout.html", {})


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
    return render(request, "knowledge_bank/register.html", context)
