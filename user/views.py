from rest_auth.registration.views import RegisterView
from rest_auth.views import LoginView
from django.views import View
from django.http import JsonResponse, HttpResponse
from .serializers import UserLoginSerializer
from django.contrib.auth.models import User
from django.contrib import auth
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib import messages
import allauth
import requests
import urllib
import .models import User

from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
#from . import forms, models, mixins

class UserLoginView(LoginView):
    serializer_class = UserLoginSerializer
    

def testlogin(request):
    return render(request, 'main.html')

class KakaoLoginView(View):
    def get(self, request):
        client_id = settings.KAKAO_KEY
        redirect_uri = "http://127.0.0.1:8000/user/kakao/login/callback/"
        return redirect(
            f"https://kauth.kakao.com/oauth/authorize?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code"
        )



class KakaoLoginCallbackView(View):
    def get(self, request):
        # access token 받기
        kakao_access_code = request.GET.get('code')
        url = 'https://kauth.kakao.com/oauth/token'
        headers = {
            'Content-type': 'application/x-www-form-urlencoded;charset=utf-8'
        }
        body = {
            'grant_type': 'authorization_code',
            'client_id': settings.KAKAO_KEY,
            'redirect_url': 'https://127.0.0.1:8000/user/kakao/login/callback',
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
        """
        # 사용자가 이미 존재할 때
        if User.objects.filter(email = email).exists():
            user = User.objects.get(email = email)
            token = jwt.encode({"email" : email}, SECRET_KEY, algorithm = "HS256")
            token = token.decode("utf-8")

            return JsonResponse({"token" : token}, status=200)
        # 처음 로그인 하는 User 추가
        else :
            User(
                kakao_id = kakao_id,
                email    = email,
                username = username
            ).save()

            token = jwt.encode({"email" : email}, SECRET_KEY, algorithm = "HS256")
            token = token.decode("utf-8")
            #return redirect()
            return JsonResponse({"token" : token}, status = 200)
        """
 

        return HttpResponse(user_data['kakao_account']['email'])
        """
        try:
            #인가코드 : 이 코드를 통해 Access token 등을 받을 수 있음
            code = request.GET.get("code")
            client_id = settings.KAKAO_KEY
            UserInfoURL="https://kapi.kakao.com/v2/user/me"
            redirect_uri="http://127.0.0.1:8000/user/kakao/login/callback"
            token_request = requests.post(
                f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={client_id}&redirect_uri={redirect_uri}&code={code}",
                #headers={"Accept":"application/json"},
            )

            #json에 access_token 포함되어 옴
            token_json = token_request.json()
            
            error = token_json.get("error",None)

            if error is not None :
                return JsonResponse({"message": "INVALID_CODE",
                "error content" : error}, status = 400)

            
            #url = 'https://kauth.kakao.com/oauth/token'


            #redirect_uri = "http://127.0.0.1:8000/user/kakao/login/callback/"
            

            #headers = {'Content_type': 'application/x-www-form-urlencoded; charset=utf-8'}

            #body = {'grant_type' : 'authorization_code',
            #'client_id': client_id,
            #'redirect_uri' : redirect_uri,
            #'code': code}
            #카카오로부터 요청받기 원하는 정보(우리는 Access token)를 얻기 위해 카카오에 보냄
            #token_kakao_res=request.post(url, headers=headers, data=body)
       
            # access token 할당
            access_token = token_json.get("access_token")
            #------get kakaotalk profile info------#
            
            profile_request = requests.get(
                UserInfoURL, headers={"Authorization" : f"Bearer {access_token}"},
            )

            profile_json = profile_request.json()
            print(profile_json)
            kakao_account = profile_response.get("properties")
            #email = kakao_account.get("email", None)
            nickname = profile_json.get("nickname")

            if nickname is None:
                raise 

        except KeyError:
            return JsonResponse({"message" : "INVALID_TOKEN"}, status = 400)

        except access_token.DoesNotExist:
            return JsonResponse({"message" : "INVALID_TOKEN"}, status = 400)
        
        # 사용자가 이미 존재할 때
        if User.objects.filter(kakao_id = kakao_id).exists():
            user = User.objects.get(kakao_id = kakao_id)
            token = jwt.encode({"email" : email}, SECRET_KEY, algorithm = "HS256")
            token = token.decode("utf-8")

            return JsonResponse({"token" : token}, status=200)
        # 처음 로그인 하는 User 추가
        else :
            User(
                kakao_id = kakao_id,
                email    = email,
                username = username
            ).save()

            token = jwt.encode({"email" : email}, SECRET_KEY, algorithm = "HS256")
            token = token.decode("utf-8")
            #return redirect()
            return JsonResponse({"token" : token}, status = 200)

        """