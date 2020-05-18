#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Time: 2020/04/30 16:56:39
# Contact: androllen#hotmail.com


from rest_framework import serializers, response
from django.utils import timezone
from .models import Exp
import datetime


class ExpSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exp
        fields = '__all__'
