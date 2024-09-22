"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from knowledge_bank import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # Route to knowledge bank homepage
    path("knowledge_bank/", include("knowledge_bank.urls"), name="knowledge-bank-home"),
    # Route to register page
    path("register/", views.register, name="register"),
    # Route to user's profile page
    path("profile/", views.profile, name="profile"),
    # Route to login page
    # redirect_authenticated_user argument ensures that already logged in users are redirected when they try to access login/
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="knowledge_bank/login.html", redirect_authenticated_user=True
        ),
        name="login",
    ),
    # Route to logout page
    path("logout/", views.user_logout, name="logout"),
    path("", include("knowledge_bank.urls")),
]

# If we are currently in debug mode. Then this is how we add media to our url patterns
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# Otherwise if in production then do it this way...
