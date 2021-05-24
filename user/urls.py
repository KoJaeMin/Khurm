from django.urls import path
from . import views
from django.urls import include, path
import rest_auth
from user.views import UserLoginView, UserUpdateView, UserInfoView

urlpatterns = [
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('signup/', include('rest_auth.registration.urls')),
    path('login/', UserLoginView.as_view()),
    path('logout/', rest_auth.views.LogoutView.as_view()),
    path('details/', UserInfoView.as_view()),  # 유저 프로필 조회
    path('update/', UserUpdateView.as_view()),  # 유저 프로필 수정
    # path('test/',views.testlogin, name='login')
]
