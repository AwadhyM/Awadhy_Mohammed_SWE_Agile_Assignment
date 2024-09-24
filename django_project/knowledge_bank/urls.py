"""
URL configuration for Knowledge Bank application.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""
from django.urls import path
from .views import (
    ArticleCreateView,
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
)

urlpatterns = [
    # Route to article list view
    path("", ArticleListView.as_view(), name="knowledge-bank-home"),
    # Route to article detail view
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article-detail"),
    # Route to page for creating a new article
    path("article/new/", ArticleCreateView.as_view(), name="article-create"),
    # Route to page for updating a new article
    path("article/update/<int:pk>", ArticleUpdateView.as_view(), name="article-update"),
    # Route to page for deleting an article
    path("article/<int:pk>/delete", ArticleDeleteView.as_view(), name="article-delete"),
]
