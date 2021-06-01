from django.urls import path
from . import views
from django.urls import include, path
import rest_auth
from user.views import UserLoginView, KakaoLoginView, KakaoLoginCallbackView, UserUpdateView, UserInfoView,UserDeleteView

app_name = "user"

urlpatterns = [
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('signup/', include('rest_auth.registration.urls')),
    path('login/', UserLoginView.as_view()),
    path('kakao/login', KakaoLoginView.as_view(), name="kakao-login"),
    path("kakao/login/callback/", KakaoLoginCallbackView.as_view(), name="kakao-login-callback"),
    path('logout/', rest_auth.views.LogoutView.as_view()),
    path('detail/', rest_auth.views.UserDetailsView.as_view()),
    path('test/',views.testlogin, name='login'),
    path('details/', UserInfoView.as_view()),  # 유저 프로필 조회
    path('update/', UserUpdateView.as_view()),  # 유저 프로필 수정
    path('delete/', UserDeleteView.as_view()), # 회원 탈퇴
    path('test/',views.testlogin, name='login'),
]
