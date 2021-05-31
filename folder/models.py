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
    # owner = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='user', db_column='f_owner')#, default=User.username)
    owner = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='file', null=True)

    f_tag = models.CharField('남녀명수', max_length=200, default='None')

    file = models.FileField(upload_to=get_upload_path, default='media/test.txt')

    class Meta:
        ordering = ['created']
        verbose_name_plural = 'Files'


def get_gender_count(file_dir):
    headers = {'X-NCP-APIGW-API-KEY-ID': 'pd89qvpcjt',
               'X-NCP-APIGW-API-KEY': 'XVMxNAF7y9XBKsfLYLRlFKliMu6XR998YxmxA7DU'}

    res = requests.post(url='https://naveropenapi.apigw.ntruss.com/vision/v1/face', files={"image": open(file_dir, "rb")}, headers=headers)
    
    male = 0
    female = 0
    jres = json.loads(res.text)
    for i in jres['faces']:
        if i['gender']['value'] == "male":
            male += 1
        else:
            female+= 1
    
    return str(male)+"/"+str(female)

class Shared(models.Model):
    user_no = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shared')
    file_no = models.ForeignKey(File, on_delete=models.CASCADE, related_name='shared')
    auth = models.CharField('권한(R/W)', max_length=100, default='R', null=False)

    class Meta:
        unique_together = ('user_no', 'file_no') # 유저와 파일 번호 묶어서 유니크로 변경

class Favorite(models.Model):
    user_no = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite')
    file_no = models.ForeignKey(File, on_delete=models.CASCADE, related_name='favorite')

    class Meta:
        unique_together = ('user_no', 'file_no')