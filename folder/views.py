from django.shortcuts import render

# Create your views here.

def filelist(request):
    return render(request,'main.html')