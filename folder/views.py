from django.shortcuts import render
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework import viewsets, parsers
from .models import File
from .serializers import FileSerializer
from rest_framework.request import Request
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.utils.functional import SimpleLazyObject
from django.contrib.auth.models import AnonymousUser

from rest_framework.decorators import action
from rest_framework.response import Response



class FileViewset(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
        
        



