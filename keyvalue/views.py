from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from rest_framework import permissions, response, viewsets, mixins, status
from .models import KeyValue
from .serializers import KeyValueSerializer
from rest_framework.decorators import action
import datetime
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.parsers import FileUploadParser
from rest_framework.views import APIView
from rest_framework.response import Response

class KeyValueViewSet(mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):

    queryset = KeyValue.objects.all()
    serializer_class = KeyValueSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def list(self, request):
        get = request.GET
        # 获取参数
        key_name = get.get('key')

        key_type = get.get('type')
        # 获取参数
        key_source = get.get('source')
        # 获取参数
        start_date = get.get('start_date', default=datetime.datetime.now())
        # 获取参数
        end_date = get.get('end_date', default=datetime.datetime.now())

        # start_date = datetime.datetime(2020, 1, 1, 12, 4, 0)2020-04-01
        # end_date = datetime.datetime(2020, 5, 7, 12, 5, 0)2020-06-01

        if isinstance(key_name, str) and isinstance(key_source, str) and isinstance(key_type, str):
            # 如果参数不为空
            if not (key_name.strip() is None) and not (key_source.strip() is None) and not(key_type.strip() is None):
                # 执行filter()方法
                queryset = KeyValue.objects.filter(
                    name__contains=key_name, sources__contains=key_source, types__contains=key_type, create_time__range=(start_date, end_date))
            else:
                # 如果参数为空，执行all()方法
                queryset = KeyValue.objects.all()
        else:
            queryset = KeyValue.objects.all()

        serializer = KeyValueSerializer(queryset, many=True)
        # 最后返回经过序列化的数据
        return response.Response(serializer.data)

    # api/mul_delete/?query=1,2,3 action装饰器使 mul_delete 方法接受delete操作
    @action(methods=['delete'], detail=False)
    def mul_delete(self, request, *args, **kwargs):
        delete_id = request.query_params.get('query', None)
        if not delete_id:
            return Response(status=status.HTTP_404_NOT_FOUND)

        ids = delete_id.split(',')
        ids = [int(x) for x in ids if x.split()]
        queryset = KeyValue.objects.filter(id__in=ids).delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)
