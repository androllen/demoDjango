#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://github.com/encode/django-rest-framework/blob/10dbf1316f/tests/test_serializer.py
# Time: 2020/04/16 12:03:15
# Contact: androllen#hotmail.com

from rest_framework import serializers, response
from .models import MyUser, MyGroup
from django.http import JsonResponse


# add yourself field
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = [
            'username', 'real_name', 'tel', 'department', 'remark', 'creator',
            'role', 'which_group', 'user_session_key'
        ]

    # 点击post
    def to_internal_value(self, data):
        username = data.get('username')
        real_name = data.get('real_name')

        # Perform the data validation.
        if not username:
            raise serializers.ValidationError(
                {'username': 'This field is required.'})

        if not real_name:
            raise serializers.ValidationError(
                {'player_name': 'This field is required.'})

        # Return the validated values. This will be available as
        # the `.validated_data` property.
        jsondata = MyUser.objects.all()
        return JsonResponse(json_dumps_params=jsondata)

    # def update(self, instance, validated_data):
    #     return MyUser.objects.update(**validated_data)

    # def to_representation(self, instance):
    #     return {'score': instance.username, 'player_name': instance.real_name}

    def create(self, validated_data):
        return MyUser.objects.create(**validated_data)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyGroup
        fields = [
            'groupname', 'group_type', 'group_info', 'sourcenum', 'creatime'
        ]
