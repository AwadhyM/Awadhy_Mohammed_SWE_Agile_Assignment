from os import walk
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
