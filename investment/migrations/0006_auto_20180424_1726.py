# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0005_auto_20180419_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactionwarning',
            name='address_type',
            field=models.IntegerField(default=1, verbose_name='\u5730\u5740\u7c7b\u578b', choices=[(1, '\u8d5a\u94b1\u8d26\u6237'), (2, '\u97ed\u83dc\u8d26\u6237')]),
        ),
    ]
