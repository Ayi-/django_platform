# -*- coding:utf-8 -*-
# ****************************************************************#
# ScriptName:
# Author: Eli
# Create Date:2015-07-13 14:56:09
# Modify Author:
# Modify Date:
# Function: 模型函数
# ****************************************************************#
from __future__ import unicode_literals
import datetime

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

from django.core import validators

from django.db import models

from django.utils import timezone
from django.utils.six import python_2_unicode_compatible

from django.utils.translation import ugettext_lazy as _
# Create your models here.

@python_2_unicode_compatible
class Permission(models.Model):
    """
    权限管理
    """
    name = models.CharField(_(u'权限名'), max_length=255, unique=True)  # 权限名
    code = models.IntegerField(_(u'权限代码'), unique=True)  # 权限代码

    class Meta:
        app_label = 'app'
        db_table = 'permission'

    def __str__(self):
        return '%s %d' % (self.name, self.code)


@python_2_unicode_compatible
class Company(models.Model):
    """
    隶属公司权限管理
    """
    name = models.CharField(_(u'名称'), max_length=255, unique=True)

    class Meta:
        app_label = 'app'
        db_table = 'company'

    def __str__(self):
        return '%s' % self.name


class UserManeger(BaseUserManager):
    def _create_user(self, username, email, password,
                     is_staff, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.localtime(timezone.now())
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        return self._create_user(username, email, password, False,
                                 **extra_fields)


@python_2_unicode_compatible
class User(AbstractBaseUser):
    username = models.CharField(_(u'用户名'), max_length=30, unique=True, default=None,
                                help_text=_(u'名字要求30个字符以内。必须为字母以及数字组合'),
                                validators=[
                                    validators.RegexValidator(r'^[\w]+$', _(u'输入用户名'), 'invalid'),
                                ],
                                error_messages={
                                    'unique': _(u"用户名已经存在"),
                                })
    full_name = models.CharField(_(u'用户全名'), max_length=30, blank=True)
    email = models.EmailField(_(u'电子邮箱'), max_length=255,
                              unique=True, blank=True)

    company = models.ForeignKey(Company, default=None)
    permission = models.ForeignKey(Permission, default=None)

    date_joined = models.DateTimeField(_(u'创建时间'), default=timezone.now)  # 用户创建时间
    #setting = models.TextField()
    objects = UserManeger()

    # use by admin
    is_staff = False

    USERNAME_FIELD = 'user'
    REQUIRED_FIELDS = ['email', 'full_name', 'company', 'permission']

    class Meta:
        verbose_name = _(u'用户表')
        verbose_name_plural = verbose_name
        app_label = 'app'
        db_table = 'user'

    def set_last_time(self):
        self.last_login = timezone.now()
        self.save()

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    # use by admin
    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):  # __unicode__ on Python 2
        return self.username

    # use by admin
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    # use by admin
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True


# 设备抽象表
class AbstractBaseEquipment(models.Model):
    name = models.CharField(_(u'设备名'), max_length=255)
    typecode = models.CharField(_(u'设备型号'), max_length=100, default=None)
    supplier = models.IntegerField(_(u'生产厂商ID'))
    price = models.IntegerField(_(u'设备价格'), default=0)
    rent_flag = models.BooleanField(_(u'租借标志'), default=False)
    maintenance_flag = models.BooleanField(_(u'维修标志'), default=False)
    last_maintenance = models.DateTimeField(_(u'最近一次维修时间'), default=None)
    production_date = models.DateTimeField(_(u'出厂日期'), default=timezone.now)
    equip_sd_argument = models.TextField(_(u'标准设备参数'))

    def get_list(self):
        raise NotImplementedError(u'继承自AbstractBaseEquipment的子类必须提供get_list()函数')

    class Meta:
        abstract = True


# 位置抽象类
class AbstractBasePosition(models.Model):
    gps_position = models.CharField(_(u'GPS位置'), max_length=100, default=0)
    geo_position = models.CharField(_(u'地理位置'), max_length=100, default=0)

    def get_gps_position(self):
        return self.gps_position

    def get_geo_position(self):
        return '%s' % self.geo_position

    class Meta:
        abstract = True


class EquipmentForConstructionMachine(AbstractBaseEquipment, AbstractBasePosition):

    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)

        d = {}
        for attr in fields:
            if isinstance(getattr(self, attr),datetime.datetime):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d %H:%M:%S')
            elif isinstance(getattr(self, attr),datetime.date):
                d[attr] = getattr(self, attr).strftime('%Y-%m-%d')
            else:
                d[attr] = getattr(self, attr)

        import json

        # return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))
        return d


    def get_list(self):
        List = [getattr(self,f.name)  for f in self._meta.fields]
        List[7]=timezone.localtime(List[7]).strftime('%Y-%m-%d %H:%M:%S')
        List[8]=timezone.localtime(List[8]).strftime('%Y-%m-%d %H:%M:%S')
        return List

    def get_dict(self):
        Dict = self.__dict__
        Dict.pop('_state','')
        Dict['equip_sd_argument']=Dict['equip_sd_argument'].replace('\n',r'<br/>')

        Dict['last_maintenance'] = timezone.localtime(Dict['last_maintenance']).strftime('%Y-%m-%d %H:%M:%S')
        Dict['production_date'] = timezone.localtime(Dict['production_date']).strftime('%Y-%m-%d %H:%M:%S')
        return Dict

    class Meta:
        db_table = 'equipment'
        verbose_name = u'工程机械设备表'
        verbose_name_plural = verbose_name


class CMWSManeger(models.Manager):
    def _create_cmws(self, equipid, temperature, envtemp,
                     state, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        cmws = self.model(temperature=temperature,
                          envtemp=envtemp, state=state,
                          state_date=now, **extra_fields)
        cmws.equipid = EquipmentForConstructionMachine.objects.get(id=equipid)
        cmws.save()
        return cmws

    def create_cmws(self, equipid, temperature, envtemp,state, **extra_fields):
        return self._create_cmws(equipid, temperature, envtemp, state,
                                 **extra_fields)


class ConstructionMachineWorkState(AbstractBasePosition):
    equipid = models.ForeignKey(EquipmentForConstructionMachine,verbose_name = u'设备号',)
    temperature = models.FloatField(_(u'当前设备内部温度'))
    envtemp = models.FloatField(_(u'当前工作环境温度'))
    state_date = models.DateTimeField(_(u'时间'),default=timezone.now)
    state = models.CharField(_(u'工作状态'), max_length=4)

    objects = CMWSManeger()

    def get_dict(self):
        Dict = self.__dict__
        Dict.pop('_state','')

        Dict['state_date'] = timezone.localtime(Dict['state_date']).strftime('%Y-%m-%d %H:%M:%S')

        return Dict

    class Meta:
        db_table = 'cm_work_state'
        verbose_name = u'设备表'
        verbose_name_plural = verbose_name


class AbstractBaseRent(models.Model):
    rental = models.FloatField(_(u'租金'))
    rental_unit = models.CharField(_(u'租金单位'),max_length=30)
    start_time = models.DateTimeField(_(u'租借起始时间'), default=timezone.now)
    end_time = models.DateTimeField(_(u'租借结束时间'), default=None)

    occupant_id = models.IntegerField(_(u'设备拥有者id'))
    tenant_id = models.IntegerField(_(u'租借者id'))

    class Meta:
        abstract = True


class CMRent(AbstractBaseRent):
    equip_id = models.ForeignKey(EquipmentForConstructionMachine)  # 租借设备id

    class Meta:
        db_table = 'cm_rent'
        verbose_name = u'租借表'
        verbose_name_plural = verbose_name


class AbstractBaseMaintenance(models.Model):
    maintenance_man = models.ForeignKey
    maintenance_equip = models.ForeignKey
    start_date = models.DateTimeField(_(u'设备维护开始时间'), default=timezone.now)
    end_date = models.DateTimeField(_(u'设备维护结束时间'), default=None)
    reason = models.TextField(_(u'设备维护原因'), default=None)

    class Meta:
        abstract = True


class CMMaintenance(AbstractBaseMaintenance):
    maintenance_equip = models.ForeignKey(EquipmentForConstructionMachine)
    maintenance_man = models.ForeignKey(User)

    class Meta:
        db_table = 'cm_maintenance'
        verbose_name = u'工程机械维护表'
        verbose_name_plural = verbose_name


# 自定义认证
class MyCustomBackend:
    def authenticate(self, username=None, password=None):
        from django import forms
        try:
            user = User.objects.get(username=username)

        except User.DoesNotExist:
            pass
        else:
            if user.check_password(password):
                return user

            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
