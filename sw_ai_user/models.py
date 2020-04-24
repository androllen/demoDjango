#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Time: 2020/04/17 16:27:41
# Contact: androllen#hotmail.com

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, PermissionsMixin, UserManager


class GroupChoice(object):
    NOGROUP = 0
    MANAGE = 1
    NORMAL = 2


class RoleChoice(object):
    ORDINARY = 1
    ADMINISTRATOR = 2
    AUDITOR = 3
    GROUPMANAGER = 4


class MyGroup(models.Model):
    class Meta():
        db_table = 'mygroup'

    TAG_GROUP_CHOICE = ((GroupChoice.NOGROUP, '未分组'),
                        (GroupChoice.MANAGE, '管理组'),
                        (GroupChoice.NORMAL, '普通组'))

    groupname = models.CharField(max_length=50, verbose_name='组名', default='')
    group_type = models.IntegerField(verbose_name='组类型',
                                     default=GroupChoice.NORMAL,
                                     choices=TAG_GROUP_CHOICE)
    group_info = models.TextField(verbose_name='组描述信息', default='')
    sourcenum = models.IntegerField(verbose_name='资源数', default=10)  # 任务最大并发数
    creatime = models.DateTimeField(verbose_name='创建时间', default=timezone.now)


class MyUser(User, PermissionsMixin):
    class Meta():
        db_table = 'myuser'

    def __str__(self):
        return self.get_username()

    TAG_ROLE_CHOICE = (
        (RoleChoice.ORDINARY, '普通用户'),
        (RoleChoice.ADMINISTRATOR, '管理员'),
        (RoleChoice.AUDITOR, '审核员'),
        (RoleChoice.GROUPMANAGER, '组管理员'),
    )

    real_name = models.CharField(max_length=50,
                                 verbose_name='姓名',
                                 default='',
                                 null=True,
                                 blank=True)
                                 
    tel = models.TextField(verbose_name='联系电话',
                           max_length=20, null=True, blank=True)

    department = models.CharField(verbose_name='部门',
                                  max_length=100,
                                  default='',
                                  null=True,
                                  blank=True)
    remark = models.CharField(verbose_name='备注',
                              max_length=200,
                              default='',
                              null=True,
                              blank=True)
    creator = models.CharField(verbose_name='创建者',
                               default='',
                               null=True,
                               max_length=50,
                               blank=True)
    role = models.IntegerField(verbose_name='用户角色',
                               default=RoleChoice.ORDINARY,
                               choices=TAG_ROLE_CHOICE)

    which_group = models.ForeignKey(MyGroup,
                                    verbose_name='用户归属组',
                                    on_delete=models.SET_DEFAULT,
                                    default=GroupChoice.NORMAL)
    user_session_key = models.TextField(verbose_name='记录用户session_key',
                                        default='')

    objects = UserManager()
    USERNAME_FIELD = 'username'


# class InviteCode(models.Model):
#     invite_code = models.CharField(max_length=60)
#     generate_time = models.DateTimeField(verbose_name='生成时间',
#                                          default=timezone.now)
#     is_used = models.BooleanField(verbose_name='是否被使用', default=False)
#     bind_user = models.ForeignKey(settings.AUTH_USER_MODEL,
#                                   verbose_name='绑定用户',
#                                   on_delete=models.CASCADE,
#                                   null=True)

