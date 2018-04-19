# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usercenter', '0006_auto_20180419_1023'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribe',
            name='coin_type',
            field=models.CharField(default=b'LTC', max_length=32, verbose_name='\u5e01\u79cd', db_index=True, choices=[(b'BTC', b'BTC'), (b'BCH', b'BCH'), (b'ETH', b'ETH'), (b'LTC', b'LTC')]),
        ),
    ]
