"""
URL configuration for User Management application.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
"""
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import (
    CustomUserDeleteView,
    CustomUserUpdateView,
    CustomUserDetailView,
)
from .views import user_logout, register

urlpatterns = [
    # Route to register page
    path("register/", register, name="register"),
    # Route to article list view
    # Route to login page
    # redirect_authenticated_user argument ensures that already logged in users are redirected when they try to access login/
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="user_management/login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
    # Route to user modification page
    path(
        "profile_modify/<int:userid>",
        CustomUserUpdateView.as_view(),
        name="profile-modify",
    ),
    # Route to user deletion page
    path("<int:pk>/delete", CustomUserDeleteView.as_view(), name="profile-delete"),
    # Route to profile detail view
    path("<int:userid>", CustomUserDetailView.as_view(), name="profile-detail"),
    # Route to logout page
    path("logout/", user_logout, name="logout"),
]
