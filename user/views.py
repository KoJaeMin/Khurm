from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView
from django.views import View
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from rest_auth.views import PasswordChangeView
from rest_auth.views import UserDetailsView
from rest_framework.generics import DestroyAPIView

from .serializers import UserLoginSerializer
from .serializers import UserUpdateSerializer, UserInfoSerializer
from user.models import User
from django.contrib import auth
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
import allauth
import requests
import urllib
import jwt
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated

from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.views import LoginView
#from . import forms, models, mixins

from allauth.socialaccount.providers.kakao.views import KakaoOAuth2Adapter
from allauth.socialaccount.providers.naver.views import NaverOAuth2Adapter
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from json.decoder import JSONDecodeError
from rest_framework import status


class KakaoLogin(SocialLoginView):
    adapter_class = KakaoOAuth2Adapter
    client_class = OAuth2Client###
    callback_url = "http://127.0.0.1:8000/user/kakao/login/callback/"

    
class NaverLogin(SocialLoginView):
    adapter_class = NaverOAuth2Adapter


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

def mainlogin(request):
    return render(request, 'main.html')

@login_required
def GoHome(request):
    return render(request, 'home.html')


def mainmodify(request):
    token=request.session.get('token','eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Im5hbWVzYWNlQGtha2FvLmNvbSIsImV4cCI6MTYyMzI2MjkwMSwiZW1haWwiOiJuYW1lc2FjZUBrYWthby5jb20iLCJvcmlnX2lhdCI6MTYyMjY1ODEwMX0.PbsWsdJzdoUMNPInZb5Szf_VtLKPaI4U9UsfF4OICU0')
    # print("token : " + jwt.decode(token,"django-insecure-j36p+5o0v$(fb)2pgvfgo*wxeo_21*^s#xekayh(_^^m)ai&4#",algorithm="HS256"))
    # token=request.COOKIES.get('token')
    decode = jwt.decode(token,"django-insecure-j36p+5o0v$(fb)2pgvfgo*wxeo_21*^s#xekayh(_^^m)ai&4#",algorithm="HS256")
    # print("userid = " + decode["user_id"].__str__())
    user = get_object_or_404(User,pk=decode["user_id"])
    return render(request, 'modify.html',{'user':user})

class KakaoLoginView(View):
    def get(self, request):
        client_id = settings.KAKAO_KEY
        redirect_uri = "http://127.0.0.1:8000/user/kakao/login/callback/"
        return redirect(
            f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
        )



class KakaoLoginCallbackView(View):
    def get(self, request):
        success_url = settings.LOGIN_REDIRECT_URL
        # access token 받기
        kakao_access_code = request.GET.get('code')
        url = 'https://kauth.kakao.com/oauth/token'
        headers = {
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        }
        body = {
            'grant_type': 'authorization_code',
            'client_id': settings.KAKAO_KEY,
            'redirect_url': 'http://127.0.0.1:8000/user/kakao/login/callback',
            'code': kakao_access_code
        }
        kakao_reponse = requests.post(url, headers=headers, data=body)
        #  front 에서 받아야 할 역할 완료 /

        data = kakao_reponse.json()
        access_token = data['access_token']
        print('access token >>', access_token)

        # user info 받기
        url = 'https://kapi.kakao.com/v2/user/me'

        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        }
        kakao_response = requests.post(url, headers=headers)

        user_data = kakao_response.json()
        kakao_id = user_data['id']
        username = user_data['properties']['nickname']
        email = user_data['kakao_account']['email']
        token_url='http://127.0.0.1:8000/user/rest-auth/kakao/'
        data = {"access_token" : access_token}
        accept = requests.post(token_url,json=data)
        accept_status = accept.status_code
        print(accept.json())
        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signup'}, status=accept_status)
        # user의 pk, email, first name, last name과 Access Token, Refresh token 가져옴
        accept_json = accept.json()
#        accept_json.pop('user', None)

        return HttpResponseRedirect(success_url)
#        return JsonResponse(accept_json)

        # try:
        #     # 사용자가 이미 존재할 때
        #     if User.objects.filter(email = email).exists():
        #         user = User.objects.get(email = email)
        #         #token = jwt.encode({"email" : email}, settings.SECRET_KEY, algorithm = "HS256")
        #         #print("token encode :", token)
        #         #token = token.decode("utf-8")
        #         #print("token decode :", token)
        #         return HttpResponseRedirect(success_url)
        #     # 처음 로그인 하는 User 추가
        #     else :
        #         User(
        #             email    = email,
        #             username = kakao_id
        #         ).save()
        # except KeyError:    
        #     return JsonResponse({"message": "INVALID_KEYS"}, status = 400)


class NaverLoginView(View):
    def get(self, request):
        client_id = settings.NAVER_ID
        redirect_uri = "http://127.0.0.1:8000/user/naver/login/callback/"
        state = 'RANDOM_STATE'#request.GET.get("csrfmiddlewaretoken")
        return redirect(
            f"https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id={client_id}&state={state}&redirect_uri={redirect_uri}"
        )


class NaverLoginCallbackView(View):
    def get(self, request):
        success_url = settings.LOGIN_REDIRECT_URL

        # URL: /members/naver-login/
        # Secret값: API개요의 Client secret
        code = request.GET.get('code')
        state = request.GET.get('state')
        if not code or not state:
            return HttpResponse('code또는 state가 전달되지 않았습니다')

        token_base_url = 'https://nid.naver.com/oauth2.0/token'
        token_params = {
            'grant_type': 'authorization_code',
            'client_id': settings.NAVER_ID,
            'client_secret': settings.NAVER_SECRET,
            'code': code,
            'state': state,
            'redirectURI': 'http://127.0.0.1:8000/user/naver/login/callback/',
        }
        token_url = '{base}?{params}'.format(
            base=token_base_url,
            params='&'.join([f'{key}={value}' for key, value in token_params.items()])
        )
        response = requests.get(token_url)
        access_token = response.json()['access_token']
        print(access_token)

        me_url = 'https://openapi.naver.com/v1/nid/me'
        me_headers = {
            'Authorization': f'Bearer {access_token}',
        }
        response = requests.get(me_url, headers=me_headers)
        user_info = response.json()
        email=user_info['response']['email']
        username = user_info['response']['nickname']

        token_url='http://127.0.0.1:8000/user/rest-auth/naver/'
        data = {"access_token" : access_token}
        accept = requests.post(token_url,json=data)
        accept_status = accept.status_code
        print(accept.json())
        if accept_status != 200:
            return JsonResponse({'err_msg': 'failed to signup'}, status=accept_status)
        # user의 pk, email, first name, last name과 Access Token, Refresh token 가져옴
        accept_json = accept.json()
        #accept_json.pop('user', None)
        #return JsonResponse(accept_json)

        return HttpResponseRedirect(success_url)
