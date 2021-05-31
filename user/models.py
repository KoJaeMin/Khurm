from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class User(AbstractUser):
    username = models.CharField('사용자', max_length=20, unique=True, blank=False, default='')
    email = models.EmailField(_('이메일'), unique=True)
    password = models.CharField('비밀번호', max_length=128)
    # nickname = models.CharField('별명이름', blank=True, max_length=100)
    phone = models.CharField('휴대폰번호', blank=True, max_length=100)
    birth = models.DateField('생년월일', blank=True, null=True)
    avail_storage = models.IntegerField('가용 용량', default=200)
    used_storage = models.IntegerField('사용 용량', default=0)
    kakao = models.CharField('카카오소셜', blank=True, max_length=200)
    naver = models.CharField('네이버소셜', blank=True, max_length=200)
#    u_active = models.BooleanField('활동중여부', default=True)
    #회원 탈퇴시 바로 DB에서 삭제해서 u_active 칼럼 삭제함. migrate 필요

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
