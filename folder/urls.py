from django.urls import path
from django.contrib import admin
from django.conf.urls import include
from rest_framework.routers import SimpleRouter
from .views import FileViewset

router = SimpleRouter()
router.register('', FileViewset)

urlpatterns = router.urls
