from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=12, verbose_name = '아이디')
    password = models.CharField(max_length=20, verbose_name = '비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name = '등록시간')

    def __str__(self):
        # User object 대신 나타날 문자
        return self.username

    class Meta:
        db_table = 'test_user'