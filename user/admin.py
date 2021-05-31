from django.contrib import admin
from .models import User
# Register your models here.

#class UserAdmin(admin.ModelAdmin):
    # 관리자 페이지에서 볼 col 설정
#    list_display = ('username', 'password')

admin.site.register(User)#, UserAdmin)