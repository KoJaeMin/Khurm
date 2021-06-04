from django.urls import path
from django.contrib import admin
from django.conf.urls import include
from rest_framework.routers import SimpleRouter
from .views import *

router = SimpleRouter()
router.register('accounts', FileViewset)
router.register('face_count', FileViewset_byface)
router.register('search', FileViewset_search)
router.register('shared', SharedViewset)
# router는 url패턴에 추가하는 방식과 다르게 마지막에 / 입력하면 오류

urlpatterns = router.urls