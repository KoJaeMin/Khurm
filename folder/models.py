from django.db import models
from django.contrib.auth.models import User
import os
# Create your models here.

def get_upload_path(instance, filename):
    return os.path.join(
      "user_%d" % instance.owner.id, instance.file_path, filename)

def get_upload_path(instance, filename):
    return os.path.join(
      "user_%d" % instance.owner.id, instance.file_path, filename)

class File(models.Model):
    
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null = True)
    title = models.CharField(max_length=30, default='default')
    file_path = models.CharField(max_length=200, default='.')
    # file_type = models.CharField(max_length=20, default='None')
    file = models.FileField(upload_to=get_upload_path,default='media/test.txt')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created']
        verbose_name_plural = 'Files'

