#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://github.com/encode/django-rest-framework/blob/10dbf1316f/tests/test_serializer.py
# Time: 2020/04/16 12:03:15
# Contact: androllen#hotmail.com

from rest_framework import serializers, response
from .models import MyUser, MyGroup
from django.http import JsonResponse
import json


# add yourself field
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyGroup
        fields = '__all__'
