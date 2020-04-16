#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Time: 2020/04/16 12:03:15
# Contact: androllen#hotmail.com

from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'created', 'name', 'describe', 'price', 'isDelete']
