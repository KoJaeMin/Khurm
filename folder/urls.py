from django.urls import path
from django.contrib import admin
from django.conf.urls import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #user/이하의 url들은 user폴더의 urls 파일에서 관리함
    path('user/', include('user.urls')),
    path('', views.filelist, name='filelist'),
]