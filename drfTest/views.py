#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Time: 2020/04/16 14:05:05
# Contact: androllen#hotmail.com

from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
# Create your views here.


class GetMessageView(APIView):

    def get(self, request):
        get = request.GET
        a = get.get('a')
        d = {'status': a, 'message': 'success'}
        return JsonResponse(d)
