from django.db import models
# Create your models here.


class dictsType(object):
    password = 1
    wifi = 2
    web = 3


class defaultType(object):
    no = False
    yes = True


class sourceType(object):
    system = 1
    manual = 2


class KeyValue(models.Model):

    class Meta():
        db_table = 'keyvalue'

    TAG_CHOICE_TYPE = ((dictsType.password, '密码字典'),
                       (dictsType.wifi, 'wifi字典'),
                       (dictsType.web, 'web字典'),
                       )

    TAG_CHOICE_DEFAULT = ((defaultType.yes, '是'),
                          (defaultType.no, '否'),
                          )

    TAG_CHOICE_SOURCE = ((sourceType.system, '系统'),
                         (sourceType.manual, '手动'),
                         )

    name = models.CharField(max_length=50, verbose_name='字典名称', default='')

    types = models.SmallIntegerField(
        verbose_name='字典类型', choices=TAG_CHOICE_TYPE, default=dictsType.password)

    defaults = models.SmallIntegerField(
        verbose_name='默认字典', choices=TAG_CHOICE_DEFAULT, default=defaultType.yes)

    sources = models.SmallIntegerField(
        verbose_name='字典来源', choices=TAG_CHOICE_SOURCE, default=sourceType.system)

    create_time = models.DateTimeField(
        auto_now=True, verbose_name='添加时间')

    description = models.CharField(max_length=150, verbose_name='字典描述')
    # https://www.jianshu.com/p/82cb876bb426
    # https://www.jianshu.com/p/610893a91f62
    # file upload
    url = models.FileField(null=True, upload_to='keyvalue',
                           blank=False, verbose_name='file url')
