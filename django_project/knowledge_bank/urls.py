"""
URL configuration for Knowledge Bank application.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Path to home page
    path("", views.home, name="knowledge-bank-home"),
]
