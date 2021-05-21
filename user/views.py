from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView
from .serializers import UserLoginSerializer
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render

#class UserRegisterView(RegisterView):
#    serializer_class = UserRegisterSerializer

class UserLoginView(LoginView):
    serializer_class = UserLoginSerializer

def testlogin(request):
    return render(request, 'main.html')