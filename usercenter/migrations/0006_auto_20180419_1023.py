# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usercenter', '0005_auto_20180329_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscribe',
            name='category',
            field=models.CharField(default=b'position', max_length=32, verbose_name='\u8ba2\u9605\u7c7b\u578b', db_index=True, choices=[(b'position', '\u6301\u4ed3\u8ba2\u9605'), (b'transaction', '\u4ea4\u6613\u8ba2\u9605')]),
        ),
    ]
