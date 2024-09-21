from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import Article


def home(request):
    """Routes user to the home page where all records will be displayed"""
    context = {"articles": Article.objects.all()}

    # Load html for home page
    return render(request, "knowledge_bank/home.html", context)


def register(request):
    """Routes user to registration page where they can register an account"""

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account successfully created for {username}")
            return redirect("knowledge-bank-home")
    else:
        form = UserRegistrationForm()

    context = {"form": form}
    return render(request, "knowledge_bank/register.html", context)
