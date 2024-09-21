from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


def home(request):
    """Routes user to the home page where all records will be displayed"""
    content = {"articles": Article.objects.all()}

    # Load html for home page
    return render(request, "knowledge_bank/home.html", content)
