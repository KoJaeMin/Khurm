from django.shortcuts import render
from rest_framework import viewsets, parsers, status
from .models import File, Shared, User
from .serializers import FileSerializer, SharedSerializer

class FileViewset(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    lookup_fields = ['owner', 'file']

    def perform_create(self, serializer):
        uploaded = self.request.FILES['file']
        uploaded = str(uploaded).split('.')

        if uploaded[1] == 'png' or uploaded[1] == 'jpg':
            serializer.save(owner = self.request.user, file_type = uploaded[1], f_tag = '네이버 api 결과값')
        else:
            serializer.save(owner = self.request.user, file_type = uploaded[1])

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(owner=self.request.user)
        return query_set


class FileViewset_byface(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def get_queryset(self):
        queryset = self.queryset
        type = ''
        no = 0
        if 'male' in self.request.query_params.keys() and 'female' in self.request.query_params.keys():
             #female과 male에 대한 쿼리파라미터가 있으면
            genderinfo = self.request.query_params['male'] + '/' + self.request.query_params['female']

        return queryset.filter(f_tag=genderinfo)

class FileViewset_search(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def get_queryset(self):
        queryset = self.queryset
        search_keyword = self.request.query_params['key']
        search_type = self.request.query_params['type']

        if 'type' in self.request.query_params.keys() and 'key' in self.request.query_params.keys():
            #type과 key에 대한 쿼리파라미터가 있으면
            queryset = queryset.filter(file_type=search_type)
            queryset = queryset.filter(text__icontains=search_keyword)

        return queryset


class SharedViewset(viewsets.ModelViewSet):
    queryset = Shared.objects.all()
    serializer_class = SharedSerializer

    def perform_create(self, serializer): # post(공유 추가) 오버라이드
        if self.request.data['auth']=='R':
            serializer.save(user_no=User.objects.get(id=self.request.data['user_no']),
                            file_no=File.objects.get(f_no=self.request.data['file_no']))
        elif self.request.data['auth']=='W':
            serializer.save(user_no=User.objects.get(id=self.request.data['user_no']),
                            file_no=File.objects.get(f_no=self.request.data['file_no']), auth='W')

    def get_queryset(self):
        queryset = self.queryset
        type = ''
        no = 0
        if 'type' in self.request.query_params.keys(): #type 쿼리파라미터가 있으면
            type = self.request.query_params['type']
        if 'no' in self.request.query_params.keys(): #no 쿼리파라미터가 있으면
            no = self.request.query_params['no']

        if type=='user': # 유저기준으로 공유되어있는 파일 필터링
            return queryset.filter(user_no=User.objects.get(id=no))
        elif type=='file':# 파일기준으로 공유되어 있는 유저 필터링
            return queryset.filter(file_no=File.objects.get(f_no=no))
        elif type=='my': # 로그인한 유저에게 공유되어 있는 레코드 필터링
            return queryset.filter(user_no=self.request.user)

        return queryset



