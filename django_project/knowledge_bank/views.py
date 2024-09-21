from django.shortcuts import render
from django.http import HttpResponse


articles = [
    {
        "author": "Awadhy Mohammed",
        "role": "Apprentice Software Engineer",
        "content": "First Article",
        "date": "October 11 2024",
    },
    {
        "author": "Awadhy Mohammed",
        "role": "Apprentice Software Engineer",
        "content": "Second Article",
        "date": "October 12 2024",
    },
]


def home(request):
    """Routes user to the home page where all records will be displayed"""
    content = {"articles": articles}

    # Load html for home page
    return render(request, "knowledge_bank/home.html", content)
