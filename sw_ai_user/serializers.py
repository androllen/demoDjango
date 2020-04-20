#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Time: 2020/04/16 12:03:15
# Contact: androllen#hotmail.com

from rest_framework import serializers
from .models import MyUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = [
            'real_name', 'tel', 'department', 'remark', 'creator', 'role',
            'which_group', 'user_session_key'
        ]
