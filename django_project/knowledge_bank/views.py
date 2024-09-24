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
from .models import Article


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
    fields = [
        "title",
        "category",
        "content",
    ]

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
    fields = ["title", "content", "category"]

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
