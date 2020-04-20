from django.shortcuts import render
from .models import MyUser ,MyGroup
from rest_framework import viewsets, response
from .serializers import UserSerializer ,GroupSerializer
from django.http import HttpResponse


class UserViewSet(viewsets.ModelViewSet):
    # import pdb
    # pdb.set_trace()
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    # import pdb
    # pdb.set_trace()
    queryset = MyGroup.objects.all()
    serializer_class = GroupSerializer
