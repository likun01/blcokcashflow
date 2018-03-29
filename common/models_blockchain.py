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


class BitBalanceTmp(models.Model):
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    sum_in_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_out_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_count = models.IntegerField(blank=True, null=True)
    sum_out_count = models.IntegerField(blank=True, null=True)
    address_type = models.SmallIntegerField(blank=True, null=True)
    last_transaction_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bit_balance_tmp'


class BitBalanceTmpTest(models.Model):
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    sum_in_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_out_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_count = models.IntegerField(blank=True, null=True)
    sum_out_count = models.IntegerField(blank=True, null=True)
    address_type = models.SmallIntegerField(blank=True, null=True)
    last_transaction_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bit_balance_tmp_test'


class BitBalanceTmpYom(models.Model):
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    sum_in_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_out_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_count = models.IntegerField(blank=True, null=True)
    sum_out_count = models.IntegerField(blank=True, null=True)
    balance_rank = models.BigIntegerField(blank=True, null=True)
    in_volume_rank = models.BigIntegerField(blank=True, null=True)
    out_volume_rank = models.BigIntegerField(blank=True, null=True)
    address_type = models.SmallIntegerField(blank=True, null=True)
    last_transaction_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bit_balance_tmp_yom'


class BitDatelist(models.Model):
    bit_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_status = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bit_datelist'


class BitErrorblocklist(models.Model):
    id = models.BigIntegerField(primary_key=True)
    blockhash = models.CharField(max_length=64, blank=True, null=True)
    next_blockhash = models.CharField(max_length=64, blank=True, null=True)
    previous_blockhash = models.CharField(max_length=64, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    nonce = models.BigIntegerField(blank=True, null=True)
    timestamp = models.IntegerField(blank=True, null=True)
    block_time = models.DateTimeField(blank=True, null=True)
    median_timestamp = models.IntegerField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    stripped_size = models.IntegerField(blank=True, null=True)
    chainwork = models.CharField(max_length=64, blank=True, null=True)
    merkleroot = models.CharField(max_length=64, blank=True, null=True)
    n_confirmations = models.IntegerField(blank=True, null=True)
    difficulty = models.DecimalField(
        max_digits=20, decimal_places=5, blank=True, null=True)
    bits = models.CharField(max_length=32, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    version_hex = models.CharField(max_length=64, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bit_errorblocklist'


class BitMarketStat(models.Model):
    btc_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    avg_transaction_volume_24h = models.DecimalField(
        db_column='avg_transaction_volume_24H', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    transaction_volume_24h = models.DecimalField(
        db_column='transaction_volume_24H', max_digits=20, decimal_places=10, blank=True, null=True)
    avg_transaction_count_24h = models.IntegerField(
        db_column='avg_transaction_count_24H', blank=True, null=True)  # Field name made lowercase.
    btc_transaction_count_24h = models.IntegerField(
        db_column='btc_transaction_count_24H', blank=True, null=True)  # Field name made lowercase.
    unconfirmed_transaction_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    unconfirmed_transaction_count = models.IntegerField(blank=True, null=True)
    address_count = models.BigIntegerField(blank=True, null=True)
    his_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bit_market_stat'


class BitMarketStatHis(models.Model):
    btc_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    avg_transaction_volume_24h = models.DecimalField(
        db_column='avg_transaction_volume_24H', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    transaction_volume_24h = models.DecimalField(
        db_column='transaction_volume_24H', max_digits=20, decimal_places=10, blank=True, null=True)
    avg_transaction_count_24h = models.IntegerField(
        db_column='avg_transaction_count_24H', blank=True, null=True)  # Field name made lowercase.
    btc_transaction_count_24h = models.IntegerField(
        db_column='btc_transaction_count_24H', blank=True, null=True)  # Field name made lowercase.
    unconfirmed_transaction_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    unconfirmed_transaction_count = models.IntegerField(blank=True, null=True)
    address_count = models.BigIntegerField(blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bit_market_stat_his'


class BitRunningStatus(models.Model):
    status = models.CharField(max_length=64, blank=True, null=True)
    status_type = models.CharField(max_length=64, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bit_running_status'


class BitRunningStatusHis(models.Model):
    status = models.CharField(max_length=64, blank=True, null=True)
    status_type = models.CharField(max_length=64, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bit_running_status_his'


class BitcoinBlockFile(models.Model):
    id = models.BigIntegerField(primary_key=True)
    filename = models.CharField(max_length=255, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitcoin_block_file'


class BitcoinBlockchain(models.Model):
    id = models.BigIntegerField(primary_key=True)
    blockhash = models.CharField(
        unique=True, max_length=64, blank=True, null=True)
    next_blockhash = models.CharField(max_length=64, blank=True, null=True)
    previous_blockhash = models.CharField(max_length=64, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    nonce = models.BigIntegerField(blank=True, null=True)
    timestamp = models.IntegerField(blank=True, null=True)
    block_time = models.DateTimeField(blank=True, null=True)
    median_timestamp = models.IntegerField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    stripped_size = models.IntegerField(blank=True, null=True)
    chainwork = models.CharField(max_length=64, blank=True, null=True)
    merkleroot = models.CharField(max_length=64, blank=True, null=True)
    n_confirmations = models.IntegerField(blank=True, null=True)
    difficulty = models.DecimalField(
        max_digits=20, decimal_places=5, blank=True, null=True)
    bits = models.CharField(max_length=32, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    version_hex = models.CharField(max_length=64, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitcoin_blockchain'


class BitcoinBlockchainRealtime(models.Model):
    id = models.BigIntegerField(primary_key=True)
    blockhash = models.CharField(
        unique=True, max_length=64, blank=True, null=True)
    next_blockhash = models.CharField(max_length=64, blank=True, null=True)
    previous_blockhash = models.CharField(max_length=64, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    nonce = models.BigIntegerField(blank=True, null=True)
    timestamp = models.IntegerField(blank=True, null=True)
    block_time = models.DateTimeField(blank=True, null=True)
    median_timestamp = models.IntegerField(blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    stripped_size = models.IntegerField(blank=True, null=True)
    chainwork = models.CharField(max_length=64, blank=True, null=True)
    merkleroot = models.CharField(max_length=64, blank=True, null=True)
    n_confirmations = models.IntegerField(blank=True, null=True)
    difficulty = models.DecimalField(
        max_digits=20, decimal_places=5, blank=True, null=True)
    bits = models.CharField(max_length=32, blank=True, null=True)
    version = models.IntegerField(blank=True, null=True)
    version_hex = models.CharField(max_length=64, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitcoin_blockchain_realtime'


class BitcoinCashflow(models.Model):
    address = models.CharField(max_length=64, blank=True, null=True)
    block_time = models.DateTimeField(blank=True, null=True)
    input_value = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    output_value = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitcoin_cashflow'


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


class BitcoinCashflowOutput24H(models.Model):
    id = models.BigIntegerField(primary_key=True)
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
        db_table = 'bitcoin_cashflow_output_24h'


class BitcoinCashflowOutputRealtime(models.Model):
    id = models.BigIntegerField(primary_key=True)
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
        db_table = 'bitcoin_cashflow_output_realtime'


class BitcoinCashflowRealtime(models.Model):
    id = models.BigIntegerField(primary_key=True)
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
        db_table = 'bitcoin_cashflow_realtime'


class BitcoinCashflowSumYom(models.Model):
    address = models.CharField(max_length=64, blank=True, null=True)
    trans_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    in_value = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    out_value = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    in_count = models.SmallIntegerField(blank=True, null=True)
    out_count = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitcoin_cashflow_sum_yom'


class BitcoinCashflowSumYom1(models.Model):
    address = models.CharField(max_length=64, blank=True, null=True)
    trans_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    in_value = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    out_value = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    in_count = models.SmallIntegerField(blank=True, null=True)
    out_count = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitcoin_cashflow_sum_yom_1'


class BitcoinTmpBalancerank(models.Model):
    id = models.BigIntegerField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitcoin_tmp_balancerank'


class BitcoinTransactionInput(models.Model):
    id = models.BigIntegerField(primary_key=True)
    blockhash = models.CharField(max_length=64, blank=True, null=True)
    transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
    input_transaction_uuid = models.CharField(
        max_length=64, blank=True, null=True)
    coinbase = models.CharField(max_length=128, blank=True, null=True)
    vout = models.IntegerField(blank=True, null=True)
    txinwitness = models.TextField(blank=True, null=True)
    block_time = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    value = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitcoin_transaction_input'


class BitcoinTransactionInputRealtime(models.Model):
    id = models.BigIntegerField(primary_key=True)
    blockhash = models.CharField(max_length=64, blank=True, null=True)
    transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
    input_transaction_uuid = models.CharField(
        max_length=64, blank=True, null=True)
    coinbase = models.CharField(max_length=128, blank=True, null=True)
    vout = models.IntegerField(blank=True, null=True)
    txinwitness = models.TextField(blank=True, null=True)
    block_time = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    value = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitcoin_transaction_input_realtime'


class BitcoinTransactionOutput(models.Model):
    id = models.BigIntegerField(primary_key=True)
    blockhash = models.CharField(max_length=64, blank=True, null=True)
    transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
    value = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    req_sigs = models.IntegerField(blank=True, null=True)
    output_type = models.CharField(max_length=64, blank=True, null=True)
    addresses = models.CharField(max_length=64, blank=True, null=True)
    block_time = models.DateTimeField(blank=True, null=True)
    foundinput = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitcoin_transaction_output'


class BitcoinTransactionOutputRealtime(models.Model):
    id = models.BigIntegerField(primary_key=True)
    blockhash = models.CharField(max_length=64, blank=True, null=True)
    transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
    value = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    index = models.IntegerField(blank=True, null=True)
    req_sigs = models.IntegerField(blank=True, null=True)
    output_type = models.CharField(max_length=64, blank=True, null=True)
    addresses = models.CharField(max_length=64, blank=True, null=True)
    block_time = models.DateTimeField(blank=True, null=True)
    foundinput = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitcoin_transaction_output_realtime'


class BitcoinUnconfirmedCashflow(models.Model):
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
        db_table = 'bitcoin_unconfirmed_cashflow'


class BitcoinUnconfirmedTransactionsInput(models.Model):
    id = models.BigIntegerField(primary_key=True)
    transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
    sequence = models.CharField(max_length=64, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    addresses = models.CharField(max_length=64, blank=True, null=True)
    hex_data = models.CharField(max_length=64, blank=True, null=True)
    relayed_by = models.CharField(max_length=32, blank=True, null=True)
    relayed_time = models.DateTimeField(blank=True, null=True)
    scrapy_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitcoin_unconfirmed_transactions_input'
        unique_together = (('transaction_uuid', 'addresses'),)


class BitcoinUnconfirmedTransactionsOutput(models.Model):
    id = models.BigIntegerField(primary_key=True)
    transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    addresses = models.CharField(max_length=64, blank=True, null=True)
    hex_data = models.CharField(max_length=64, blank=True, null=True)
    relayed_by = models.CharField(max_length=32, blank=True, null=True)
    relayed_time = models.DateTimeField(blank=True, null=True)
    scrapy_time = models.DateTimeField(blank=True, null=True)
    blockhash = models.CharField(max_length=45, blank=True, null=True)
    output_index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bitcoin_unconfirmed_transactions_output'
        unique_together = (('transaction_uuid', 'output_index'),)


class ChangeAddressList(models.Model):
    address = models.CharField(max_length=64, blank=True, null=True)
    change_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'change_address_list'


class LitecoinChartsDatas(models.Model):
    id = models.BigIntegerField(primary_key=True)
    price_usd = models.FloatField(blank=True, null=True)
    price_btc = models.FloatField(blank=True, null=True)
    hisdate = models.DateField(unique=True, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'litecoin_charts_datas'


class TBit24InvolumeRank1000His(models.Model):
    ranking = models.AutoField(primary_key=True)
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
    # Field renamed because it wasn't a valid Python identifier.
    number_24h_trans_volume = models.DecimalField(
        db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_7d_trans_volume = models.DecimalField(
        db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_30d_trans_volume = models.DecimalField(
        db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    unconfirmed_trans_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_24involume_rank1000_his'


class TBit24InvolumeRank1000Newrank(models.Model):
    ranking = models.AutoField(primary_key=True)
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
    # Field renamed because it wasn't a valid Python identifier.
    number_24h_trans_volume = models.DecimalField(
        db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_7d_trans_volume = models.DecimalField(
        db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_30d_trans_volume = models.DecimalField(
        db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    unconfirmed_trans_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_24involume_rank1000_newrank'


class TBit24InvolumeRank1000Now(models.Model):
    ranking = models.AutoField(primary_key=True)
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
    # Field renamed because it wasn't a valid Python identifier.
    number_24h_trans_volume = models.DecimalField(
        db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_7d_trans_volume = models.DecimalField(
        db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_30d_trans_volume = models.DecimalField(
        db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    unconfirmed_trans_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_24involume_rank1000_now'


class TBit24InvolumeRank1000Yom(models.Model):
    ranking = models.AutoField(primary_key=True)
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
    # Field renamed because it wasn't a valid Python identifier.
    number_24h_trans_volume = models.DecimalField(
        db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_7d_trans_volume = models.DecimalField(
        db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_30d_trans_volume = models.DecimalField(
        db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    unconfirmed_trans_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_24involume_rank1000_yom'


class TBit24OutvolumeRank1000His(models.Model):
    ranking = models.AutoField(primary_key=True)
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
    # Field renamed because it wasn't a valid Python identifier.
    number_24h_trans_volume = models.DecimalField(
        db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_7d_trans_volume = models.DecimalField(
        db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_30d_trans_volume = models.DecimalField(
        db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    unconfirmed_trans_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_24outvolume_rank1000_his'


class TBit24OutvolumeRank1000Newrank(models.Model):
    ranking = models.AutoField(primary_key=True)
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
    # Field renamed because it wasn't a valid Python identifier.
    number_24h_trans_volume = models.DecimalField(
        db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_7d_trans_volume = models.DecimalField(
        db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_30d_trans_volume = models.DecimalField(
        db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    unconfirmed_trans_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_24outvolume_rank1000_newrank'


class TBit24OutvolumeRank1000Now(models.Model):
    ranking = models.AutoField(primary_key=True)
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
    # Field renamed because it wasn't a valid Python identifier.
    number_24h_trans_volume = models.DecimalField(
        db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_7d_trans_volume = models.DecimalField(
        db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_30d_trans_volume = models.DecimalField(
        db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    unconfirmed_trans_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_24outvolume_rank1000_now'


class TBit24OutvolumeRank1000Yom(models.Model):
    ranking = models.AutoField(primary_key=True)
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
    # Field renamed because it wasn't a valid Python identifier.
    number_24h_trans_volume = models.DecimalField(
        db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_7d_trans_volume = models.DecimalField(
        db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_30d_trans_volume = models.DecimalField(
        db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    unconfirmed_trans_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_24outvolume_rank1000_yom'


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


class TBitBalanceRank1000Newrank(models.Model):
    ranking = models.AutoField(primary_key=True)
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

    class Meta:
        managed = False
        db_table = 't_bit_balance_rank1000_newrank'


class TBitBalanceRank1000Now(models.Model):
    ranking = models.AutoField(primary_key=True)
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

    class Meta:
        managed = False
        db_table = 't_bit_balance_rank1000_now'


class TBitBalanceRank1000Realtime(models.Model):
    ranking = models.AutoField(primary_key=True)
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

    class Meta:
        managed = False
        db_table = 't_bit_balance_rank1000_realtime'


class TBitBalanceRank1000Yom(models.Model):
    ranking = models.AutoField(primary_key=True)
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
        db_table = 't_bit_balance_rank1000_yom'


class TBitBalancechangeRank1000His(models.Model):
    ranking = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_24h_balancechange = models.DecimalField(
        db_column='24h_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_7d_balancechange = models.DecimalField(
        db_column='7d_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_30d_balancechange = models.DecimalField(
        db_column='30d_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)
    unconfirmed_balancechange = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_balancechange_rank1000_his'


class TBitBalancechangeRank1000Newrank(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_24h_balancechange = models.DecimalField(
        db_column='24h_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_7d_balancechange = models.DecimalField(
        db_column='7d_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_30d_balancechange = models.DecimalField(
        db_column='30d_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)
    unconfirmed_balancechange = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_balancechange_rank1000_newrank'


class TBitBalancechangeRank1000Now(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_24h_balancechange = models.DecimalField(
        db_column='24h_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_7d_balancechange = models.DecimalField(
        db_column='7d_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_30d_balancechange = models.DecimalField(
        db_column='30d_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)
    unconfirmed_balancechange = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_balancechange_rank1000_now'


class TBitBalancechangeRank1000Yom(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_24h_balancechange = models.DecimalField(
        db_column='24h_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_7d_balancechange = models.DecimalField(
        db_column='7d_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_30d_balancechange = models.DecimalField(
        db_column='30d_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)
    unconfirmed_balancechange = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_balancechange_rank1000_yom'


class TBitBalancetransRankHis(models.Model):
    ranking = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    transaction_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    transaction_count = models.IntegerField(blank=True, null=True)
    last_transaction_datetime = models.DateTimeField(blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_balancetrans_rank_his'


class TBitBalancetransRankNewrank(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    transaction_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    transaction_count = models.IntegerField(blank=True, null=True)
    last_transaction_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_balancetrans_rank_newrank'


class TBitBalancetransRankNow(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    transaction_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    transaction_count = models.IntegerField(blank=True, null=True)
    last_transaction_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_balancetrans_rank_now'


class TBitBalancetransRankYom(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    transaction_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    transaction_count = models.IntegerField(blank=True, null=True)
    last_transaction_datetime = models.DateTimeField(blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_balancetrans_rank_yom'


class TBitIncountRank1000His(models.Model):
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
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_incount_rank1000_his'


class TBitIncountRank1000Newrank(models.Model):
    ranking = models.AutoField(primary_key=True)
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

    class Meta:
        managed = False
        db_table = 't_bit_incount_rank1000_newrank'


class TBitIncountRank1000Now(models.Model):
    ranking = models.AutoField(primary_key=True)
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

    class Meta:
        managed = False
        db_table = 't_bit_incount_rank1000_now'


class TBitIncountRank1000Yom(models.Model):
    ranking = models.AutoField(primary_key=True)
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
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_incount_rank1000_yom'


class TBitNotransRank1000His(models.Model):
    ranking = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    last_transaction_datetime = models.DateTimeField(blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_notrans_rank1000_his'


class TBitNotransRank1000Now(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    last_transaction_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_notrans_rank1000_now'


class TBitNotransRank1000Yom(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    last_transaction_datetime = models.DateTimeField(blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_notrans_rank1000_yom'


class TBitOutcountRank1000His(models.Model):
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
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_outcount_rank1000_his'


class TBitOutcountRank1000Newrank(models.Model):
    ranking = models.AutoField(primary_key=True)
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

    class Meta:
        managed = False
        db_table = 't_bit_outcount_rank1000_newrank'


class TBitOutcountRank1000Now(models.Model):
    ranking = models.AutoField(primary_key=True)
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

    class Meta:
        managed = False
        db_table = 't_bit_outcount_rank1000_now'


class TBitOutcountRank1000Yom(models.Model):
    ranking = models.AutoField(primary_key=True)
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
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_outcount_rank1000_yom'


class TBitSumIncountRank1000His(models.Model):
    ranking = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_out_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_transcount = models.IntegerField(blank=True, null=True)
    sum_out_transcount = models.IntegerField(blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_sum_incount_rank1000_his'


class TBitSumIncountRank1000Newrank(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_out_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_transcount = models.IntegerField(blank=True, null=True)
    sum_out_transcount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_sum_incount_rank1000_newrank'


class TBitSumIncountRank1000Now(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_out_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_transcount = models.IntegerField(blank=True, null=True)
    sum_out_transcount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_sum_incount_rank1000_now'


class TBitSumIncountRank1000Yom(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_out_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_transcount = models.IntegerField(blank=True, null=True)
    sum_out_transcount = models.IntegerField(blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_sum_incount_rank1000_yom'


class TBitSumInvolumeRank1000His(models.Model):
    ranking = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_out_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_transcount = models.IntegerField(blank=True, null=True)
    sum_out_transcount = models.IntegerField(blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_sum_involume_rank1000_his'


class TBitSumInvolumeRank1000Newrank(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_out_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_transcount = models.IntegerField(blank=True, null=True)
    sum_out_transcount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_sum_involume_rank1000_newrank'


class TBitSumInvolumeRank1000Now(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_out_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_transcount = models.IntegerField(blank=True, null=True)
    sum_out_transcount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_sum_involume_rank1000_now'


class TBitSumInvolumeRank1000Yom(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_out_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_transcount = models.IntegerField(blank=True, null=True)
    sum_out_transcount = models.IntegerField(blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_sum_involume_rank1000_yom'


class TBitSumOutcountRank1000His(models.Model):
    ranking = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_out_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_transcount = models.IntegerField(blank=True, null=True)
    sum_out_transcount = models.IntegerField(blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_sum_outcount_rank1000_his'


class TBitSumOutcountRank1000Newrank(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_out_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_transcount = models.IntegerField(blank=True, null=True)
    sum_out_transcount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_sum_outcount_rank1000_newrank'


class TBitSumOutcountRank1000Now(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_out_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_transcount = models.IntegerField(blank=True, null=True)
    sum_out_transcount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_sum_outcount_rank1000_now'


class TBitSumOutcountRank1000Yom(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_out_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_transcount = models.IntegerField(blank=True, null=True)
    sum_out_transcount = models.IntegerField(blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_sum_outcount_rank1000_yom'


class TBitSumOutvolumeRank1000His(models.Model):
    ranking = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_out_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_transcount = models.IntegerField(blank=True, null=True)
    sum_out_transcount = models.IntegerField(blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_sum_outvolume_rank1000_his'


class TBitSumOutvolumeRank1000Newrank(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_out_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_transcount = models.IntegerField(blank=True, null=True)
    sum_out_transcount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_sum_outvolume_rank1000_newrank'


class TBitSumOutvolumeRank1000Now(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_out_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_transcount = models.IntegerField(blank=True, null=True)
    sum_out_transcount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_sum_outvolume_rank1000_now'


class TBitSumOutvolumeRank1000Yom(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_out_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    sum_in_transcount = models.IntegerField(blank=True, null=True)
    sum_out_transcount = models.IntegerField(blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_sum_outvolume_rank1000_yom'


class TBitTransactionVolume10Minute(models.Model):
    transaction_time = models.DateTimeField(primary_key=True)
    volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    miner_income = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    miner_charge = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_transaction_volume_10minute'


class TBitTransactionVolumeDay(models.Model):
    transaction_date = models.DateTimeField(primary_key=True)
    volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    miner_income = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    miner_charge = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_transaction_volume_day'


class TBitTranscountRank1000His(models.Model):
    ranking = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_24h_transaction_count = models.IntegerField(
        db_column='24h_transaction_count', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_7d_transaction_count = models.IntegerField(
        db_column='7d_transaction_count', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_30d_transaction_count = models.IntegerField(
        db_column='30d_transaction_count', blank=True, null=True)
    unconfirmed_transaction_count = models.IntegerField(blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_transcount_rank1000_his'


class TBitTranscountRank1000Newrank(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_24h_transaction_count = models.IntegerField(
        db_column='24h_transaction_count', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_7d_transaction_count = models.IntegerField(
        db_column='7d_transaction_count', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_30d_transaction_count = models.IntegerField(
        db_column='30d_transaction_count', blank=True, null=True)
    unconfirmed_transaction_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_transcount_rank1000_newrank'


class TBitTranscountRank1000Now(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_24h_transaction_count = models.IntegerField(
        db_column='24h_transaction_count', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_7d_transaction_count = models.IntegerField(
        db_column='7d_transaction_count', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_30d_transaction_count = models.IntegerField(
        db_column='30d_transaction_count', blank=True, null=True)
    unconfirmed_transaction_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_transcount_rank1000_now'


class TBitTranscountRank1000Yom(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_24h_transaction_count = models.IntegerField(
        db_column='24h_transaction_count', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_7d_transaction_count = models.IntegerField(
        db_column='7d_transaction_count', blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_30d_transaction_count = models.IntegerField(
        db_column='30d_transaction_count', blank=True, null=True)
    unconfirmed_transaction_count = models.IntegerField(blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_transcount_rank1000_yom'


class TBitTransvolumeRank1000His(models.Model):
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
    # Field renamed because it wasn't a valid Python identifier.
    number_24h_trans_volume = models.DecimalField(
        db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_7d_trans_volume = models.DecimalField(
        db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_30d_trans_volume = models.DecimalField(
        db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    unconfirmed_trans_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_transvolume_rank1000_his'


class TBitTransvolumeRank1000Newrank(models.Model):
    ranking = models.AutoField(primary_key=True)
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
    # Field renamed because it wasn't a valid Python identifier.
    number_24h_trans_volume = models.DecimalField(
        db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_7d_trans_volume = models.DecimalField(
        db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_30d_trans_volume = models.DecimalField(
        db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    unconfirmed_trans_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_transvolume_rank1000_newrank'


class TBitTransvolumeRank1000Now(models.Model):
    ranking = models.AutoField(primary_key=True)
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
    # Field renamed because it wasn't a valid Python identifier.
    number_24h_trans_volume = models.DecimalField(
        db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_7d_trans_volume = models.DecimalField(
        db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_30d_trans_volume = models.DecimalField(
        db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    unconfirmed_trans_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_transvolume_rank1000_now'


class TBitTransvolumeRank1000Yom(models.Model):
    ranking = models.AutoField(primary_key=True)
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
    # Field renamed because it wasn't a valid Python identifier.
    number_24h_trans_volume = models.DecimalField(
        db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_7d_trans_volume = models.DecimalField(
        db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    # Field renamed because it wasn't a valid Python identifier.
    number_30d_trans_volume = models.DecimalField(
        db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)
    unconfirmed_trans_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    his_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_transvolume_rank1000_yom'


class TBitUnconfirmedRank1000Now(models.Model):
    ranking = models.AutoField(primary_key=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    balance = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    unconfirmed_transaction_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    unconfirmed_in_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    unconfirmed_out_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)
    transaction_volume = models.DecimalField(
        max_digits=20, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_bit_unconfirmed_rank1000_now'
