#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Time: 2020/04/16 15:53:27
# Contact: androllen#hotmail.com

from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, UserViewSet

app_name = 'drfTest'

router = routers.DefaultRouter()
router.register('products', ProductViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls))
]

# urlpatterns = []
# urlpatterns += router.urls