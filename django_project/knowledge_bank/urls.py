"""
URL configuration for Knowledge Bank application.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import (
    ArticleCreateView,
    ArticleListView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView,
    CustomUserUpdateView,
    CustomUserDetailView,
)
from . import views

urlpatterns = [
    # Route to register page
    path("register/", views.register, name="register"),
    # Route to article list view
    path("", ArticleListView.as_view(), name="knowledge-bank-home"),
    # Route to login page
    # redirect_authenticated_user argument ensures that already logged in users are redirected when they try to access login/
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="knowledge_bank/login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
    path(
        "profile_modify/<int:userid>",
        CustomUserUpdateView.as_view(),
        name="profile-modify",
    ),
    # Route to profile detail view
    path("profile/<int:userid>", CustomUserDetailView.as_view(), name="profile-detail"),
    # Route to logout page
    path("logout/", views.user_logout, name="logout"),
    # Route to article detail view
    path("article/<int:pk>", ArticleDetailView.as_view(), name="article-detail"),
    # Route to page for creating a new article
    path("article/new/", ArticleCreateView.as_view(), name="article-create"),
    # Route to page for updating a new article
    path("article/update/<int:pk>", ArticleUpdateView.as_view(), name="article-update"),
    # Route to page for deleting an article
    path("article/<int:pk>/delete", ArticleDeleteView.as_view(), name="article-delete"),
]
