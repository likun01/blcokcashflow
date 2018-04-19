# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BitcoinCashflowOutput',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=64, null=True, blank=True)),
                ('block_time', models.DateTimeField(null=True, blank=True)),
                ('input_value', models.DecimalField(null=True, max_digits=20, decimal_places=10, blank=True)),
                ('output_value', models.DecimalField(null=True, max_digits=20, decimal_places=10, blank=True)),
                ('miner_charge', models.DecimalField(null=True, max_digits=20, decimal_places=10, blank=True)),
            ],
            options={
                'db_table': 'bitcoin_cashflow_output',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BitcoinChartsDatas',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('price', models.FloatField(null=True, blank=True)),
                ('hisdate', models.DateField(unique=True, null=True, blank=True)),
                ('create_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'bitcoin_charts_datas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BitExchangeRecharge',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupind', models.IntegerField()),
                ('trans_date', models.DateField(null=True, blank=True)),
                ('tot_recharge', models.DecimalField(null=True, max_digits=42, decimal_places=10, blank=True)),
                ('avg_recharge', models.DecimalField(null=True, max_digits=24, decimal_places=14, blank=True)),
            ],
            options={
                'db_table': 'bit_exchange_recharge',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BitExchangeWithdraw',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('groupind', models.IntegerField()),
                ('trans_date', models.DateField(null=True, blank=True)),
                ('tot_withdraw', models.DecimalField(null=True, max_digits=42, decimal_places=10, blank=True)),
                ('avg_with_draw', models.DecimalField(null=True, max_digits=24, decimal_places=14, blank=True)),
            ],
            options={
                'db_table': 'bit_exchange_withdraw',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='IndexHis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('index_value', models.DecimalField(null=True, max_digits=20, decimal_places=10, blank=True)),
                ('his_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'db_table': 'index_his',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TBitSpecialAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=64, null=True, blank=True)),
                ('address_type', models.IntegerField(null=True, blank=True)),
                ('start_date', models.DateField(null=True, blank=True)),
                ('end_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'db_table': 't_bit_special_address',
                'managed': False,
            },
        ),
    ]
