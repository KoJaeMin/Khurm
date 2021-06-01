from django.urls import path
from django.contrib import admin
from django.conf.urls import include
from rest_framework.routers import SimpleRouter
from .views import FileViewset, SharedViewset, FavoriteViewset

router = SimpleRouter()
router.register('accounts', FileViewset)
router.register('shared', SharedViewset)
router.register('favorite', FavoriteViewset)
# router는 url패턴에 추가하는 방식과 다르게 마지막에 / 입력하면 오류

urlpatterns = router.urls