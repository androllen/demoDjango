from django.shortcuts import render
from rest_framework import permissions, response, viewsets
from .models import Exp
from .serializers import ExpSerializer
from rest_framework.decorators import action
import datetime


class ExpViewSet(viewsets.ModelViewSet):
    queryset = Exp.objects.all()
    serializer_class = ExpSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    
    def list(self, request):
        get = request.GET
        # 获取参数
        key_name = get.get('name')
        # 获取参数
        key_source = get.get('source')
        # 获取参数
        start_date = get.get('start_date', default=datetime.datetime.now())
        # 获取参数
        end_date = get.get('end_date', default=datetime.datetime.now())

        # start_date = datetime.datetime(2020, 1, 1, 12, 4, 0)2020-04-01T15:17:10
        # end_date = datetime.datetime(2020, 5, 7, 12, 5, 0)2020-06-01

        if isinstance(key_name, str) and isinstance(key_source, str):
            # 如果参数不为空
            if not (key_name.strip() is None) and not (key_source.strip() is None):
                # 执行filter()方法
                queryset = Exp.objects.filter(
                    name__contains=key_name, source__contains=key_source, create_time__range=(start_date, end_date))
            else:
                # 如果参数为空，执行all()方法
                queryset = Exp.objects.all()
        else:
            queryset = Exp.objects.all()

        serializer = ExpSerializer(queryset, many=True)
        # 最后返回经过序列化的数据
        return response.Response(serializer.data)
