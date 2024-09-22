from os import walk
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.generic import ListView, DetailView
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from .models import Article


def home(request):
    """Routes user to the home page where all records will be displayed"""
    context = {"articles": Article.objects.all()}

    # Load html for home page
    return render(request, "knowledge_bank/home.html", context)


class ArticleListView(ListView):
    """Routes user to page displaying all records. This is achieved through
    the use of Django's ListView Class."""

    template_name = "knowledge_bank/home.html"
    model = Article
    context_object_name = "articles"
    ordering = ["date_posted"]


class ArticleDetailView(DetailView):
    """Routes user to page displaying a selected record. This is achieved through
    the use of Django's DetailView Class."""

    model = Article


def register(request):
    """Routes user to registration page where they can register an account"""

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request,
                f"Account successfully created for {username}. You can now login using the form below.",
            )
            return redirect("login")
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, "knowledge_bank/register.html", context)


@login_required
def profile(request):
    """Routes user to their profile page. If they are logged in."""
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f"Account successfully updated.")
            return redirect("profile")
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {"user_form": user_form, "profile_form": profile_form}

    return render(request, "knowledge_bank/profile.html", context)


@login_required
def user_logout(request):
    """Routes user to logout page"""
    logout(request)
    return render(request, "knowledge_bank/logout.html", {})
