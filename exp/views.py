from rest_framework import permissions, response, mixins, viewsets
from .models import Exp
from .serializers import ExpSerializer
import datetime


class ExpViewSet(mixins.RetrieveModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.ListModelMixin,
                 viewsets.GenericViewSet):

    queryset = Exp.objects.all()
    serializer_class = ExpSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        get = request.GET
        # 获取参数
        key_name = get.get('name')
        # 获取参数
        key_source = get.get('source')
        # 获取参数
        start_date = get.get('start_date', default=datetime.datetime.now())
        # 获取参数
        end_date = get.get('end_date', default=datetime.datetime.now())

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
