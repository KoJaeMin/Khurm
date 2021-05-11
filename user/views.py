from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView
from .serializers import UserLoginSerializer


#class UserRegisterView(RegisterView):
#    serializer_class = UserRegisterSerializer


class UserLoginView(LoginView):
    serializer_class = UserLoginSerializer