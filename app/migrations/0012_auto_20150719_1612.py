# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20150718_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmmaintenance',
            name='end_date',
            field=models.DateTimeField(default=None, verbose_name='\u8bbe\u5907\u7ef4\u62a4\u7ed3\u675f\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='cmmaintenance',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u8bbe\u5907\u7ef4\u62a4\u5f00\u59cb\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='cmrent',
            name='end_time',
            field=models.DateTimeField(default=None, verbose_name='\u79df\u501f\u7ed3\u675f\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='cmrent',
            name='start_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u79df\u501f\u8d77\u59cb\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='equipmentforconstructionmachine',
            name='last_maintenance',
            field=models.DateTimeField(default=None, verbose_name='\u6700\u8fd1\u4e00\u6b21\u7ef4\u4fee\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='equipmentforconstructionmachine',
            name='production_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u51fa\u5382\u65e5\u671f'),
        ),
    ]
