#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://github.com/encode/django-rest-framework/blob/10dbf1316f/tests/test_serializer.py
# Time: 2020/04/16 12:03:15
# Contact: androllen#hotmail.com

from rest_framework import serializers, response
from .models import MyUser, MyGroup
from django.http import JsonResponse
import json
from django.utils.timezone import now
from django.contrib.auth.hashers import make_password
import django.contrib.auth.password_validation as validators
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label='用户名', help_text='add', validators=[
                                     UniqueValidator(queryset=MyUser.objects.all())])
    password = serializers.CharField(
        label='密码', help_text='增加密码', required=False, allow_blank=True, style={'input_type': 'password'})

    # error_messages = {'blank': '密码不能为空', 'min_length': '密码的最小长度不能小于6个字节'}
    repassword = serializers.CharField(label='确认密码', required=False, allow_blank=True,
                                       write_only=True, min_length=6, style={'input_type': 'password'})

    class Meta:
        model = MyUser
        fields = [
            'user_ptr_id', 'username', 'real_name', 'tel', 'department', 'remark', 'password',
            'creator', 'role', 'which_group', 'repassword', 'user_session_key'
        ]

    def validate(self, attrs):
        if attrs.get('repassword') != attrs.get('password'):
            raise serializers.ValidationError('两次密码输入不一致')

        repwd = attrs.get('repassword')
        del repwd
        attrs['password'] = make_password(attrs['password'])
        return attrs

    def validate_repassword(self, value):
        request = self.context.get('request')
        pswd = request.data.get('password')
        repswd = request.data.get('repassword')

        if not pswd.strip():
            raise serializers.ValidationError('密码不能为空')

        if not repswd.strip():
            raise serializers.ValidationError('确认密码不能为空')

        if value != pswd:
            raise serializers.ValidationError('两次密码输入不一致')
        return pswd

    def create(self, validated_data):
        user = MyUser(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.password = validated_data.get('password', instance.password)
        instance.save()
        return instance


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyGroup
        fields = [
            'groupname', 'group_type', 'group_info', 'sourcenum', 'creatime'
        ]


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)  # 有可能未登录
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    class Meta:
        model = MyGroup
