# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usercenter', '0004_auto_20180323_1724'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='memberorder',
            options={'ordering': ('-created_datetime',), 'verbose_name': '\u8d2d\u4e70\u8ba2\u5355', 'verbose_name_plural': '\u8d2d\u4e70\u8ba2\u5355'},
        ),
        migrations.AddField(
            model_name='subscribe',
            name='address',
            field=models.CharField(db_index=True, max_length=64, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='subscribe',
            name='category',
            field=models.CharField(default=b'position', max_length=32, verbose_name='\u8ba2\u9605\u7c7b\u578b', choices=[(b'position', '\u6301\u4ed3\u8ba2\u9605'), (b'transaction', '\u4ea4\u6613\u8ba2\u9605')]),
        ),
    ]
