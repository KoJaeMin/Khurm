from . import views
from django.urls import include, path
from django.conf.urls import url

import rest_auth
from user.views import *
app_name = "user"

urlpatterns = [
    # path('rest-auth/registration/', include('rest_auth.registration.urls')),
    #path('signup/', include('rest_auth.registration.urls')),
    path('signup/', UserSignupView.as_view()),
    
    path('login/', UserLoginView.as_view()),
    path('/', include('rest_auth.urls')),
    
    
    path('kakao/login', KakaoLoginView.as_view(), name="kakao-login"),
    path("kakao/login/callback/", KakaoLoginCallbackView.as_view(), name="kakao-login-callback"),
    path('naver/login', NaverLoginView.as_view(), name="naver-login"),

    path('naver/login/callback/', NaverLoginCallbackView.as_view(), name="naver-login-callback"),
    path('rest-auth/kakao/', KakaoLogin.as_view(), name="kakao_login2django"),
    path('rest-auth/naver/', NaverLogin.as_view(), name="naver_login2django"),
    path('logout/', rest_auth.views.LogoutView.as_view()),
    path('detail/', rest_auth.views.UserDetailsView.as_view()),
    path('home/', GoHome),
    path('home/img_s3', GoImg),
    path('home/shared_s3', GoShared),
    path('home/favorite_s3', GoFavorite),
    path('home/test', GoS3),
    path('main/', mainlogin),
    path('modify/',mainmodify),
    path('details/', UserInfoView.as_view()),  # 유저 프로필 조회
    path('update/', UserUpdateView.as_view()),  # 유저 프로필 수정
    path('delete/', UserDeleteView.as_view()), # 회원 탈퇴

]
