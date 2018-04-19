# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investment', '0004_transactionwarning_block_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='positionwarning',
            name='coin_type',
            field=models.CharField(default=b'LTC', max_length=32, verbose_name='\u5e01\u79cd', db_index=True, choices=[(b'BTC', b'BTC'), (b'BCH', b'BCH'), (b'ETH', b'ETH'), (b'LTC', b'LTC')]),
        ),
        migrations.AddField(
            model_name='transactionwarning',
            name='coin_type',
            field=models.CharField(default=b'LTC', max_length=32, verbose_name='\u5e01\u79cd', db_index=True, choices=[(b'BTC', b'BTC'), (b'BCH', b'BCH'), (b'ETH', b'ETH'), (b'LTC', b'LTC')]),
        ),
    ]
