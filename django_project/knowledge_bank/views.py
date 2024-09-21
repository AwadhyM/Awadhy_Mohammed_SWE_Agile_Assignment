from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    """Routes user to the home page where all records will be displayed"""
    return HttpResponse("<h1> Knowledge Bank Home </h1>")
