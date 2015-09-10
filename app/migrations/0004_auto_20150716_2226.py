# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.core.validators
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150716_0724'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 16, 14, 26, 5, 643208, tzinfo=utc), verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='email', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=30, verbose_name='name', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True, help_text='\u6807\u8bb0\u7528\u6237\u662f\u5426\u6709\u6743\u9650\u767b\u9646', verbose_name='active'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='\u6807\u8bb0\u672c\u7528\u6237\u662f\u5426\u6709\u6743\u9650\u8bbf\u95ee', verbose_name='staff status'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(null=True, verbose_name='last login', blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=False, error_messages={'unique': '\u7528\u6237\u540d\u5df2\u7ecf\u5b58\u5728'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w]+$', '\u8f93\u5165\u7528\u6237\u540d', 'invalid')], help_text='\u540d\u5b57\u8981\u6c4230\u4e2a\u5b57\u7b26\u4ee5\u5185\u3002\u5fc5\u987b\u4e3a\u5b57\u6bcd\u4ee5\u53ca\u6570\u5b57\u7ec4\u5408', unique=True, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
