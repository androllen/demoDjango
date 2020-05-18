#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Time: 2020/04/16 15:53:27
# Contact: androllen#hotmail.com

from django.urls import path, include
from rest_framework import routers
from .views import ExpViewSet
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'exp'

# exp_list = ExpViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# exp_detail = ExpViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# exp_queryexps = ExpViewSet.as_view({
#     'get': 'queryexps'
# })

# urlpatterns = format_suffix_patterns([
#   path('list/', exp_list, name='exp-list'),
#   path('list/<int:pk>/', exp_detail, name='exp-detail'),
#   path('list/queryexps/',
#        exp_queryexps, name='exp-queryexps')
# ])

router = routers.DefaultRouter()
router.register('', ExpViewSet)

urlpatterns = [
    path('', include(router.urls))
]
