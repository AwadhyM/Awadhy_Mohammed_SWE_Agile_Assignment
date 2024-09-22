"""
URL configuration for Knowledge Bank application.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path
from . import views
from .views import ArticleListView, ArticleDetailView

urlpatterns = [
    # Route to home page
    # path("", views.home, name="knowledge-bank-home"),
    # Route to article list view
    path("", ArticleListView.as_view(), name="knowledge-bank-home"),
    # Route to article detail view
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article-detail"),
]
