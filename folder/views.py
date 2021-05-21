from django.shortcuts import render
from rest_framework import viewsets, parsers
from .models import File
from .serializers import FileSerializer


class FileViewset(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names=['get', 'post', 'patch', 'delete']
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)
        
        