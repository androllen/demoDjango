from .upload import MultipleFilesUpload
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import KeyValueViewSet
from .upload import MultipleFilesUpload


app_name = 'keyvalue'

router = routers.DefaultRouter()
router.register('info', KeyValueViewSet, basename='info')


urlpatterns = [
    path('', include(router.urls)),
    path('file/', MultipleFilesUpload.as_view())
]
