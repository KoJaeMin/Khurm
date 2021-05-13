from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

class CostumUser(AbstractUser):
    first_name = None
    last_name = None
    username = None
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField('비밀번호', max_length=128)
    is_active = models.BooleanField(
        _('active'),
        default=True,
    )
    date_joined = models.DateTimeField(_('가입일'), default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    nickname = models.CharField('이름', blank=False, max_length=50)
    phone = models.CharField('휴대폰번호', blank=True, max_length=100)
    birth = models.DateField('생년월일', blank=True, null=True)
    avail_storage = models.IntegerField('가용 용량', blank=False, default=200)
    used_storage = models.IntegerField('사용 용량', blank=False, default=0)
    kakao = models.CharField('카카오소셜', blank=True)
    naver = models.CharField('네이버소셜', blank=True)

    def __str__(self):
        return self.email