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


class BuyandsellWinnerList(models.Model):
    address = models.CharField(max_length=64, blank=True, null=True)
    wincount = models.DecimalField(max_digits=23, decimal_places=0, blank=True, null=True)
    count = models.BigIntegerField()
    losecount = models.DecimalField(max_digits=23, decimal_places=0, blank=True, null=True)
    winrate = models.DecimalField(max_digits=27, decimal_places=4, blank=True, null=True)
    loserate = models.DecimalField(max_digits=27, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = '_buyandsell_winner_list'


class Goodaddress(models.Model):
    address1 = models.CharField(max_length=64, blank=True, null=True)
    address2 = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'goodaddress'


class IndexBalanceHis(models.Model):
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    his_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'index_balance_his'


class IndexHis(models.Model):
    index_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    his_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'index_his'


class IndexHisBak(models.Model):
    index_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    his_date = models.DateField(blank=True, null=True)
    id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'index_his_bak'


class LiteExchangeRecharge(models.Model):
    groupind = models.IntegerField()
    trans_date = models.DateField(blank=True, null=True)
    tot_recharge = models.DecimalField(max_digits=42, decimal_places=10, blank=True, null=True)
    avg_recharge = models.DecimalField(max_digits=24, decimal_places=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lite_exchange_recharge'


class LiteExchangeWithdraw(models.Model):
    groupind = models.IntegerField()
    trans_date = models.DateField(blank=True, null=True)
    tot_withdraw = models.DecimalField(max_digits=42, decimal_places=10, blank=True, null=True)
    avg_with_draw = models.DecimalField(max_digits=24, decimal_places=14, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lite_exchange_withdraw'


class LiteKnewAddress2(models.Model):
    address = models.CharField(unique=True, max_length=64, blank=True, null=True)
    groupind = models.IntegerField()
    onoroff = models.IntegerField(blank=True, null=True)
    createtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lite_knew_address2'


class LiteMinerlist(models.Model):
    address = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lite_minerlist'


class LiteReturnAnalysis(models.Model):
    balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    sum_in_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    sum_out_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_count = models.IntegerField(blank=True, null=True)
    sum_out_count = models.IntegerField(blank=True, null=True)
    address_type = models.SmallIntegerField(blank=True, null=True)
    last_transaction_datetime = models.DateTimeField(blank=True, null=True)
    totreturn = models.DecimalField(max_digits=47, decimal_places=13, blank=True, null=True)
    totinvest = models.DecimalField(max_digits=42, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lite_return_analysis'


class LiteStockCashflow(models.Model):
    address_type = models.IntegerField(blank=True, null=True)
    his_date = models.DateField(blank=True, null=True)
    in_amount = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    out_amount = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lite_stock_cashflow'


class LiteTotalReturn(models.Model):
    ret1 = models.DecimalField(max_digits=43, decimal_places=10, blank=True, null=True)
    invest = models.DecimalField(max_digits=42, decimal_places=10, blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lite_total_return'


class LitecoinCashflowOutput(models.Model):
    address = models.CharField(max_length=64, blank=True, null=True)
    block_time = models.DateTimeField(blank=True, null=True)
    input_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    output_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    miner_charge = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'litecoin_cashflow_output'


class LitecoinCashflowOutputSelected1(models.Model):
    address = models.CharField(max_length=64, blank=True, null=True)
    block_time = models.DateTimeField(blank=True, null=True)
    input_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    output_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    miner_charge = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    transaction_date = models.DateField(blank=True, null=True)
    trans_volume_doller = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    avgcost = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    suminvolmebefore = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    transaction_return_rate = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    win_or_lose = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'litecoin_cashflow_output_selected1'


class LitecoinCashflowOutputWinneranalyst(models.Model):
    address = models.CharField(max_length=64, blank=True, null=True)
    block_time = models.DateTimeField(blank=True, null=True)
    input_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    output_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    miner_charge = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    transaction_date = models.DateField(blank=True, null=True)
    trans_volume_doller = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    avgcost = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    transaction_return_rate = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    win_or_lose = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'litecoin_cashflow_output_winneranalyst'


class LitecoinCashflowOutputWinneranalystBuyandsell(models.Model):
    address = models.CharField(max_length=64, blank=True, null=True)
    block_time = models.DateTimeField(blank=True, null=True)
    input_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    output_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    miner_charge = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    transaction_date = models.DateField(blank=True, null=True)
    trans_volume_doller = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    last_tran_price = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    transaction_return_rate = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    win_or_lose = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'litecoin_cashflow_output_winneranalyst_buyandsell'


class LitecoinCashflowOutputWinneranalystCopy(models.Model):
    address = models.CharField(max_length=64, blank=True, null=True)
    block_time = models.DateTimeField(blank=True, null=True)
    input_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    output_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    miner_charge = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    transaction_date = models.DateField(blank=True, null=True)
    trans_volume_doller = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    avgcost = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    transaction_return_rate = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    win_or_lose = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'litecoin_cashflow_output_winneranalyst_copy'


class LitecoinChartsDatas(models.Model):
    id = models.BigIntegerField(primary_key=True)
    price_usd = models.FloatField(blank=True, null=True)
    price_btc = models.FloatField(blank=True, null=True)
    hisdate = models.DateField(unique=True, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'litecoin_charts_datas'


class ProcRecord(models.Model):
    address = models.CharField(max_length=64, blank=True, null=True)
    block_time = models.DateTimeField(blank=True, null=True)
    avgcost = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'proc_record'


class TLiteBalanceRank1000His(models.Model):
    ranking = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    yesterday_balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    number_7d_balance = models.DecimalField(db_column='7d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_30d_balance = models.DecimalField(db_column='30d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_180d_balance = models.DecimalField(db_column='180d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    number_365d_balance = models.DecimalField(db_column='365d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_lite_balance_rank1000_his'


class TLiteLongtermIndex(models.Model):
    address = models.CharField(max_length=64, blank=True, null=True)
    weight = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_lite_longterm_index'


class TLiteSpecialAddress(models.Model):
    address = models.CharField(max_length=64, blank=True, null=True)
    address_type = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_lite_special_address'


class WinnerList(models.Model):
    address = models.CharField(max_length=64, blank=True, null=True)
    wincount = models.DecimalField(max_digits=23, decimal_places=0, blank=True, null=True)
    count = models.BigIntegerField()
    winrate = models.DecimalField(max_digits=27, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'winner_list'


class WinnerList1(models.Model):
    address = models.CharField(max_length=64, blank=True, null=True)
    wincount = models.DecimalField(max_digits=23, decimal_places=0, blank=True, null=True)
    count = models.BigIntegerField()
    winrate = models.DecimalField(max_digits=27, decimal_places=4, blank=True, null=True)
    b_totreturn_totinvest = models.DecimalField(db_column='b.totreturn/totinvest', max_digits=61, decimal_places=17, blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'winner_list1'
