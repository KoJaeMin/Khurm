from django.db import models
from user.models import User
import os


# Create your models here.

def get_upload_path(instance, filename):
    return os.path.join(
        "user_%d" % instance.owner.id, instance.file_path, filename)


class File(models.Model):
    f_no = models.AutoField('파일번호', primary_key=True)
    title = models.CharField('파일 이름', max_length=30, default='default', db_column='f_name')
    file_path = models.CharField('파일절대경로', max_length=200, default='.')
    file_type = models.CharField('파일 타입', max_length=20, default='None')
    created = models.DateTimeField('파일 생성일', auto_now_add=True)
    updated = models.DateTimeField('파일 최근 수정일', auto_now=True)
    f_size = models.IntegerField('파일용량', default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='file', db_column='f_owner')#, default=User.username)
    f_tag = models.CharField('남녀명수', max_length=200, default='None')

    file = models.FileField(upload_to=get_upload_path, default='media/test.txt')

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'Files'


class Shared(models.Model):
    user_no = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shared')
    file_no = models.ForeignKey(File, on_delete=models.CASCADE, related_name='shared')
    auth = models.CharField('권한(R/W)', max_length=100, default='R', null=False)


class Favorite(models.Model):
    user_no = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite')
    file_no = models.ForeignKey(File, on_delete=models.CASCADE, related_name='favorite')
