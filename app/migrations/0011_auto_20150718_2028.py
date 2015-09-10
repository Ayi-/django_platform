# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20150718_0943'),
    ]

    operations = [
        migrations.CreateModel(
            name='CMMaintenance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_date', models.DateField(default=django.utils.timezone.now, verbose_name='\u8bbe\u5907\u7ef4\u62a4\u5f00\u59cb\u65f6\u95f4')),
                ('end_date', models.DateField(default=None, verbose_name='\u8bbe\u5907\u7ef4\u62a4\u7ed3\u675f\u65f6\u95f4')),
                ('reason', models.TextField(default=None, verbose_name='\u8bbe\u5907\u7ef4\u62a4\u539f\u56e0')),
            ],
            options={
                'db_table': 'cm_maintenance',
                'verbose_name': '\u5de5\u7a0b\u673a\u68b0\u7ef4\u62a4\u8868',
                'verbose_name_plural': '\u5de5\u7a0b\u673a\u68b0\u7ef4\u62a4\u8868',
            },
        ),
        migrations.CreateModel(
            name='CMRent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rental', models.FloatField(verbose_name='\u79df\u91d1')),
                ('rental_unit', models.CharField(max_length=30, verbose_name='\u79df\u91d1\u5355\u4f4d')),
                ('start_time', models.DateField(default=django.utils.timezone.now, verbose_name='\u79df\u501f\u8d77\u59cb\u65f6\u95f4')),
                ('end_time', models.DateField(default=None, verbose_name='\u79df\u501f\u7ed3\u675f\u65f6\u95f4')),
                ('occupant_id', models.IntegerField(verbose_name='\u8bbe\u5907\u62e5\u6709\u8005id')),
                ('tenant_id', models.IntegerField(verbose_name='\u79df\u501f\u8005id')),
            ],
            options={
                'db_table': 'cm_rent',
                'verbose_name': '\u79df\u501f\u8868',
                'verbose_name_plural': '\u79df\u501f\u8868',
            },
        ),
        migrations.CreateModel(
            name='ConstructionMachineWorkState',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gps_position', models.CharField(default=None, max_length=100, verbose_name='GPS\u4f4d\u7f6e')),
                ('geo_position', models.CharField(default=None, max_length=100, verbose_name='\u5730\u7406\u4f4d\u7f6e')),
                ('temperature', models.FloatField(verbose_name='\u5f53\u524d\u8bbe\u5907\u5185\u90e8\u6e29\u5ea6')),
                ('envtemp', models.FloatField(verbose_name='\u5f53\u524d\u5de5\u4f5c\u73af\u5883\u6e29\u5ea6')),
                ('state', models.CharField(max_length=4, verbose_name='\u5de5\u4f5c\u72b6\u6001')),
            ],
            options={
                'db_table': 'cm_work_state',
                'verbose_name': '\u8bbe\u5907\u8868',
                'verbose_name_plural': '\u8bbe\u5907\u8868',
            },
        ),
        migrations.CreateModel(
            name='EquipmentForConstructionMachine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='\u8bbe\u5907\u540d')),
                ('typecode', models.CharField(default=None, max_length=100, verbose_name='\u8bbe\u5907\u578b\u53f7')),
                ('supplier', models.IntegerField(verbose_name='\u751f\u4ea7\u5382\u5546ID')),
                ('price', models.IntegerField(default=0, verbose_name='\u8bbe\u5907\u4ef7\u683c')),
                ('rent_flag', models.BooleanField(default=False, verbose_name='\u79df\u501f\u6807\u5fd7')),
                ('maintenance_flag', models.BooleanField(default=False, verbose_name='\u7ef4\u4fee\u6807\u5fd7')),
                ('last_maintenance', models.DateField(default=None, verbose_name='\u6700\u8fd1\u4e00\u6b21\u7ef4\u4fee\u65f6\u95f4')),
                ('production_date', models.DateField(default=django.utils.timezone.now, verbose_name='\u51fa\u5382\u65e5\u671f')),
                ('equip_sd_argument', models.TextField(verbose_name='\u6807\u51c6\u8bbe\u5907\u53c2\u6570')),
                ('gps_position', models.CharField(default=None, max_length=100, verbose_name='GPS\u4f4d\u7f6e')),
                ('geo_position', models.CharField(default=None, max_length=100, verbose_name='\u5730\u7406\u4f4d\u7f6e')),
            ],
            options={
                'db_table': 'equipment',
                'verbose_name': '\u5de5\u7a0b\u673a\u68b0\u8bbe\u5907\u8868',
                'verbose_name_plural': '\u5de5\u7a0b\u673a\u68b0\u8bbe\u5907\u8868',
            },
        ),
        migrations.AddField(
            model_name='constructionmachineworkstate',
            name='equipid',
            field=models.ForeignKey(to='app.EquipmentForConstructionMachine'),
        ),
        migrations.AddField(
            model_name='cmrent',
            name='equip_id',
            field=models.ForeignKey(to='app.EquipmentForConstructionMachine'),
        ),
        migrations.AddField(
            model_name='cmmaintenance',
            name='maintenance_equip',
            field=models.ForeignKey(to='app.EquipmentForConstructionMachine'),
        ),
        migrations.AddField(
            model_name='cmmaintenance',
            name='maintenance_man',
            field=models.ForeignKey(to='app.User'),
        ),
    ]
