from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == "GET": 
        return render(request, 'login2.html')

    elif request.method == "POST":
        username = request.POST.get['username', None]
        password = request.POST.get['password', None]
        re_password = request.POST.get['re_password', None]
        res_data={}

        if not (username and password and re_password):
            res_data['error'] = '모든 항목을 입력해야 합니다.'
        if password != re_password:
            res_data['error'] = '비밀번호가 일치하지 않습니다.'
        else:
            # make_password() 패스워드 암호화
            user=User(username=username, password=make_password(password))
            user.save()
        return render(request, 'signup.html', res_data)

"""
def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')
    elif request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username = request.POST["username"], password = request.POST["password1"])

            auth.login(request, user)
            return redirect('../../folder/')
        return render(request, 'signup.html', {'error': 'password does not match'})
    return render(request,'signup.html')
"""

def login(request):
     
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('../../folder/')
        else:
            return render(request, 'login.html', {'error': 'user name or password is incorrect'})

    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return render('login.html')

