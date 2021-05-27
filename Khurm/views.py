from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied

import django

def index(request):
        return render(request, "test.html")