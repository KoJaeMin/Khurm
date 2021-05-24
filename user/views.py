from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView
from rest_auth.views import PasswordChangeView
from .serializers import UserLoginSerializer
from .serializers import UserUpdateSerializer
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render


# class UserRegisterView(RegisterView):
#    serializer_class = UserRegisterSerializer

class UserLoginView(LoginView):
    serializer_class = UserLoginSerializer


# 프로필 수정
class UserUpdateView(PasswordChangeView):
    serializer_class = UserUpdateSerializer


def testlogin(request):
    return render(request, 'main.html')
