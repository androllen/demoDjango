#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Time: 2020/04/16 15:53:27
# Contact: androllen#hotmail.com

from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, GroupViewSet

app_name = 'sw_ai_user'

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [path('', include(router.urls))]
