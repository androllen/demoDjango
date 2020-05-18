from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class SourceChoice(object):
    System = 1
    Manual = 2


class Exp(models.Model):

    class Meta():
        db_table = 'experience'

    TAG_CHOICE = ((SourceChoice.System, '系统'),
                  (SourceChoice.Manual, '手动'))
    name = models.CharField(max_length=50, verbose_name='经验名称', default='')

    description = models.CharField(
        max_length=200, verbose_name='经验描述', default='')

    create_time = models.DateTimeField(
        verbose_name='创建时间', default=timezone.now)

    source = models.SmallIntegerField(
        verbose_name='经验来源', choices=TAG_CHOICE, default=SourceChoice.System)
