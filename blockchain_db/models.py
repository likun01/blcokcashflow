# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class BitExchangeRecharge(models.Model):
    groupind = models.IntegerField()
    trans_date = models.DateField(blank=True, null=True)
    tot_recharge = models.DecimalField(
        max_digits=42, decimal_places=10, blank=True, null=True)
    avg_recharge = models.DecimalField(
        max_digits=24, decimal_places=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bit_exchange_recharge'


class BitExchangeWithdraw(models.Model):
    groupind = models.IntegerField()
    trans_date = models.DateField(blank=True, null=True)
    tot_withdraw = models.DecimalField(
        max_digits=42, decimal_places=10, blank=True, null=True)
    avg_with_draw = models.DecimalField(
        max_digits=24, decimal_places=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bit_exchange_withdraw'


class BitcoinCashflowOutput(models.Model):
    address = models.CharField(max_length=64, blank=True, null=True)
    block_time = models.DateTimeField(blank=True, null=True)
    input_value = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    output_value = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    miner_charge = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitcoin_cashflow_output'


class BitcoinChartsDatas(models.Model):
    id = models.BigIntegerField(primary_key=True)
    price = models.FloatField(blank=True, null=True)
    hisdate = models.DateField(unique=True, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitcoin_charts_datas'


class BitIndexHis(models.Model):
    index_value = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    his_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bit_index_his'


class TBitSpecialAddress(models.Model):
    address = models.CharField(max_length=64, blank=True, null=True)
    address_type = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_special_address'


class TBitBalanceRank1000His(models.Model):
    ranking = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_24_in_volume = models.DecimalField(
        db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_24_out_volume = models.DecimalField(
        db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_24_in_transcount = models.IntegerField(
        db_column='24_in_transcount', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_24_out_transcount = models.IntegerField(
        db_column='24_out_transcount', blank=True, null=True)
    yesterday_balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_7d_balance = models.DecimalField(
        db_column='7d_balance', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_30d_balance = models.DecimalField(
        db_column='30d_balance', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_180d_balance = models.DecimalField(
        db_column='180d_balance', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_365d_balance = models.DecimalField(
        db_column='365d_balance', max_digits=20, decimal_places=10, blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_balance_rank1000_his'


class BitMinerlist(models.Model):
    address = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bit_minerlist'


class BitKnewAddress2(models.Model):
    address = models.CharField(
        unique=True, max_length=64, blank=True, null=True)
    groupind = models.IntegerField()
    onoroff = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bit_knew_address2'
