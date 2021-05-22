from django.shortcuts import render
from rest_framework import viewsets, parsers
from .models import File
from .serializers import FileSerializer


class FileViewset(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    lookup_fields = ['owner', 'file']
    
    def perform_create(self, serializer):
        uploaded = self.request.FILES['file']
        uploaded = str(uploaded).split('.')
        serializer.save(owner = self.request.user, file_type = uploaded[1])
        if uploaded[1] == 'png' or uploaded[1] == 'jpg':
            serializer.save(f_tag = '네이버 api 결과값')


    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(owner=self.request.user)
        return query_set