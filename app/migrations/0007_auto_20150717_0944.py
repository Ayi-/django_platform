# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150717_0918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='name')),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.RemoveField(
            model_name='group',
            name='permission',
        ),
        migrations.AddField(
            model_name='user',
            name='permission',
            field=models.ForeignKey(default=None, to='app.Permission'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=None, error_messages={'unique': '\u7528\u6237\u540d\u5df2\u7ecf\u5b58\u5728'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w]+$', '\u8f93\u5165\u7528\u6237\u540d', 'invalid')], help_text='\u540d\u5b57\u8981\u6c4230\u4e2a\u5b57\u7b26\u4ee5\u5185\u3002\u5fc5\u987b\u4e3a\u5b57\u6bcd\u4ee5\u53ca\u6570\u5b57\u7ec4\u5408', unique=True, verbose_name='username'),
        ),
        migrations.DeleteModel(
            name='Group',
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ForeignKey(default=None, to='app.Company'),
        ),
    ]
