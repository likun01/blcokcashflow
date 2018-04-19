# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0002_auto_20180329_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactionwarning',
            name='address_type',
            field=models.IntegerField(default=1, verbose_name='\u5730\u5740\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='transactionwarning',
            name='change',
            field=models.CharField(default=b'buy', max_length=14, verbose_name='\u6da8\u8dcc', choices=[(b'buy', '\u4e70\u5165'), (b'sell', '\u5356\u51fa')]),
        ),
        migrations.AlterField(
            model_name='positionwarning',
            name='pushed',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u5df2\u63a8\u9001'),
        ),
        migrations.AlterField(
            model_name='transactionwarning',
            name='pushed',
            field=models.BooleanField(default=False, db_index=True, verbose_name='\u5df2\u63a8\u9001'),
        ),
    ]
