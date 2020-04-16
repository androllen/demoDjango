#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Time: 2020/04/16 14:05:05
# Contact: androllen#hotmail.com

from django.shortcuts import render
from rest_framework import viewsets, response
from .models import Product
from .serializers import UserSerializer, ProductSerializer
from rest_framework.decorators import action
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


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