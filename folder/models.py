from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class File(models.Model):
    
    title = models.CharField(max_length=30, default='default')
    #document = models.FileField(max_length=30)
    # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    #fileData = models.FileField(upload_to='timeline_file/%Y/%m/%d', blank=False, null=False)
    image = models.ImageField(upload_to='timeline_file/%Y/%m/%d',default='media/logo.png')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created']
        verbose_name_plural = 'Files'

