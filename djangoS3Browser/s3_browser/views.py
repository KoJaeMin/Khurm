import json, requests
from typing import DefaultDict

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .operations import *
from .forms import PostForm
from folder.models import get_gender_count

"fetch the directories within the selected folder"


def get_folder_items(request, main_folder, sort_a_z):
    json_string = get_folder_with_items(main_folder, sort_a_z)
    return HttpResponse(json.dumps(json_string), content_type="application/json")


@csrf_exempt
def upload(request):

    #file model에 올리기 전 유효성 검사 피하기 위해 null이어도 되는 파트 지정
    form = PostForm(request.POST, request.FILES)
    form.fields['file_type'].required = False
    form.fields['f_tag'].required = False
    form.fields['f_size'].required = False

    # file S3에 업로드 하는 부분
    file = request.FILES.get('file')
    upload_file(request.POST.get('loc', ''), file)

    #form 유효성 체크하고 model에 정보 넣음.
    if form.is_valid():
        post = form.save()
        post.save()
        file_type = str(file).split('.')
        post.file_type = file_type[1]
        post.f_size = file.size

        post.save()

        path = settings.MEDIA_URL + request.FILES ['file'].name
        
        if file_type[1] == 'png' or file_type[1] == 'jpg':
            post.f_tag = get_gender_count(path[1:])
        else:
            post.f_tag = "None"
        
        post.save()
            
    return HttpResponse(json.dumps(file.name), content_type="application/json", status=200)


@csrf_exempt
def create_folder(request):
    create_folder_item(request.POST.get('loc', ''), request.POST.get('folder_name', ''))
    return HttpResponse(json.dumps("OK"), content_type="application/json", status=200)


@csrf_exempt
def download(request):
    file = request.GET.get('file')
    result = download_file(file)
    response = HttpResponse(result['Body'].read())
    response['Content-Type'] = result['ContentType']
    response['Content-Length'] = result['ContentLength']
    response['Content-Disposition'] = 'attachment; filename=' + file[1:]
    response['Accept-Ranges'] = 'bytes'
    return response


@csrf_exempt
def rename_file(request):
    file_name = rename(request.POST['loc'], request.POST['file'], request.POST['new_name'])
    return HttpResponse(json.dumps(file_name), content_type="application/json", status=200)


@csrf_exempt
def paste_file(request):
    paste(request.POST['loc'], request.POST.getlist('file_list[]'))
    return HttpResponse(json.dumps("OK"), content_type="application/json", status=200)


@csrf_exempt
def move_file(request):
    move(request.POST['loc'], request.POST.getlist('file_list[]'))
    return HttpResponse(json.dumps("OK"), content_type="application/json", status=200)


@csrf_exempt
def delete_file(request):
    delete(request.POST.getlist('file_list[]'))
    return HttpResponse(json.dumps("OK"), content_type="application/json", status=200)
