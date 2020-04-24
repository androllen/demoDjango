#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Time: 2020/04/16 14:05:05
# Contact: androllen#hotmail.com

from django.shortcuts import render
from rest_framework import viewsets, response
from .models import Product, comment
from .serializers import UserSerializer, ProductSerializer
from rest_framework.decorators import action
from django.contrib.auth.models import User
from drfTest.serializers import CommentSerializer
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    serializer = CommentSerializer(comment)
    print(serializer.data)

    json_data = JSONRenderer().render(serializer.data)
    print(json_data)

    stream = io.BytesIO(json_data)
    data = JSONParser().parse(stream)

    serializer = CommentSerializer(data=data)
    serializer.is_valid()
    serializer.validated_data


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    # http://127.0.0.1:8000/products/2/changeName/?newName=qwer
    @action(detail=True)
    def changeName(self, request, *args, **kwargs):
        get = request.GET
        product = self.get_object()
        product.name = get.get('newName')
        product.save()

        return response.Response(product.name)
    # http://127.0.0.1:8000/products/filterProducts/
    @action(detail=False)
    def filterProducts(self, request):
        products = Product.objects.filter(id__in=range(3))
        serializer = ProductSerializer(products, many=True)

        return response.Response(serializer.data)
