from django.shortcuts import render
from rest_framework import viewsets, parsers
from .models import File
from .serializers import FileSerializer
from rest_framework.request import Request
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.utils.functional import SimpleLazyObject
from django.contrib.auth.models import AnonymousUser



class FileViewset(viewsets.ModelViewSet):

    queryset = File.objects.all()
    serializer_class = FileSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']
