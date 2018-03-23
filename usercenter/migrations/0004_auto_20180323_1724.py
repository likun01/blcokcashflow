# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usercenter', '0003_emailecode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_member',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u662f\u5426\u4f1a\u5458'),
        ),
        migrations.AlterField(
            model_name='user',
            name='member_last_date',
            field=models.DateField(db_index=True, null=True, verbose_name='\u4f1a\u5458\u5230\u671f', blank=True),
        ),
    ]
