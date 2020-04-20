from django.shortcuts import render
from .models import MyUser
from rest_framework import viewsets
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    # import pdb
    # pdb.set_trace()
    queryset = MyUser.objects.all()
    serializer_class = UserSerializer
