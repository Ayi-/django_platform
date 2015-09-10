# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20150717_0944'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '\u7528\u6237\u8868', 'verbose_name_plural': '\u7528\u6237\u8868'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, help_text='\u6807\u8bb0\u672c\u7528\u6237\u662f\u5426\u6709\u6743\u9650\u8bbf\u95ee', verbose_name='\u8bbf\u95ee\u6807\u8bb0\u4f4d'),
        ),
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(unique=True, max_length=255, verbose_name='\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='code',
            field=models.IntegerField(unique=True, verbose_name='\u6743\u9650\u4ee3\u7801'),
        ),
        migrations.AlterField(
            model_name='permission',
            name='name',
            field=models.CharField(unique=True, max_length=255, verbose_name='\u6743\u9650\u540d'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 17, 21, 41, 48, 665843), verbose_name='\u521b\u5efa\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(unique=True, max_length=255, verbose_name='\u7535\u5b50\u90ae\u7bb1', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=30, verbose_name='\u7528\u6237\u5168\u540d', blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='\u6807\u8bb0\u7528\u6237\u662f\u5426\u6709\u6743\u9650\u767b\u9646', verbose_name='\u767b\u9646\u6807\u8bb0\u4f4d'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=None, error_messages={'unique': '\u7528\u6237\u540d\u5df2\u7ecf\u5b58\u5728'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w]+$', '\u8f93\u5165\u7528\u6237\u540d', 'invalid')], help_text='\u540d\u5b57\u8981\u6c4230\u4e2a\u5b57\u7b26\u4ee5\u5185\u3002\u5fc5\u987b\u4e3a\u5b57\u6bcd\u4ee5\u53ca\u6570\u5b57\u7ec4\u5408', unique=True, verbose_name='\u7528\u6237\u540d'),
        ),
    ]
