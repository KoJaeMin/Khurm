from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView
from rest_auth.views import PasswordChangeView
from rest_auth.views import UserDetailsView
from rest_framework.generics import DestroyAPIView

from .serializers import UserLoginSerializer
from .serializers import UserUpdateSerializer, UserInfoSerializer
from user.models import User
from django.contrib import auth
from django.shortcuts import render

#class UserRegisterView(RegisterView):
#    serializer_class = UserRegisterSerializer

class UserLoginView(LoginView):
    serializer_class = UserLoginSerializer

class UserUpdateView(PasswordChangeView):
    serializer_class = UserUpdateSerializer

class UserInfoView(UserDetailsView):
    serializer_class = UserInfoSerializer

class UserDeleteView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserInfoSerializer
    def get_object(self):
        return self.request.user

def testlogin(request):
    return render(request, 'main.html')