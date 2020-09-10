#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Time: 2020/04/30 16:56:39
# Contact: androllen#hotmail.com


from rest_framework import serializers
from .models import Exp


class ExpSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exp
        fields = '__all__'
