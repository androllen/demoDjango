#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Time: 2020/04/16 12:03:15
# Contact: androllen#hotmail.com

from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'created', 'name', 'description', 'price', 'isDelete']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_staff']


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
