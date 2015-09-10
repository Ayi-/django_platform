# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20150719_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='constructionmachineworkstate',
            name='state_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u65f6\u95f4'),
        ),
    ]
