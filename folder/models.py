from django.db import models
#from django.contrib.auth.models import User

from user.models import User

# Create your models here.
class File(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    fileData = models.FileField(upload_to='timeline_file/%Y/%m/%d', blank=False, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']