# # This is an auto-generated Django model module.
# # You'll have to do the following manually to clean this up:
# #   * Rearrange models' order
# #   * Make sure each model has one field with primary_key=True
# #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # Feel free to rename the models, but don't rename db_table values or field names.
# #
# # Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# # into your database.
# from __future__ import unicode_literals
#
# from django.db import models
#
#
# class BuyandsellWinnerList(models.Model):
#     address = models.CharField(max_length=64, blank=True, null=True)
#     wincount = models.DecimalField(max_digits=23, decimal_places=0, blank=True, null=True)
#     count = models.BigIntegerField()
#     losecount = models.DecimalField(max_digits=23, decimal_places=0, blank=True, null=True)
#     winrate = models.DecimalField(max_digits=27, decimal_places=4, blank=True, null=True)
#     loserate = models.DecimalField(max_digits=27, decimal_places=4, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = '_buyandsell_winner_list'
#
#
# class AddressSelected1(models.Model):
#     address = models.CharField(max_length=64, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'address_selected1'
#
#
# class AlertingList(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     coin_type = models.IntegerField(blank=True, null=True)
#     alert_type = models.IntegerField(blank=True, null=True)
#     alert_level = models.IntegerField(blank=True, null=True)
#     transaction_time = models.DateTimeField(blank=True, null=True)
#     create_time = models.DateTimeField(blank=True, null=True)
#     alerted = models.IntegerField(blank=True, null=True)
#     title = models.CharField(max_length=64, blank=True, null=True)
#     content = models.CharField(max_length=400, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'alerting_list'
#
#
# class BitAddressgroup4Test1(models.Model):
#     address = models.CharField(max_length=64, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_addressgroup4_test1'
#
#
# class BitAddressgroup4Test2(models.Model):
#     address = models.CharField(max_length=64, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_addressgroup4_test2'
#
#
# class BitAllGroupInputaddress(models.Model):
#     address = models.CharField(max_length=64, blank=True, null=True)
#     groupind = models.IntegerField(blank=True, null=True)
#     knewornot = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_all_group_inputaddress'
#
#
# class BitBalanceTmp(models.Model):
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     sum_in_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_out_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_count = models.IntegerField(blank=True, null=True)
#     sum_out_count = models.IntegerField(blank=True, null=True)
#     address_type = models.SmallIntegerField(blank=True, null=True)
#     last_transaction_datetime = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_balance_tmp'
#
#
# class BitBalanceTmpTest(models.Model):
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     sum_in_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_out_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_count = models.IntegerField(blank=True, null=True)
#     sum_out_count = models.IntegerField(blank=True, null=True)
#     address_type = models.SmallIntegerField(blank=True, null=True)
#     last_transaction_datetime = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_balance_tmp_test'
#
#
# class BitBalanceTmpYom(models.Model):
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     sum_in_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_out_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_count = models.IntegerField(blank=True, null=True)
#     sum_out_count = models.IntegerField(blank=True, null=True)
#     balance_rank = models.BigIntegerField(blank=True, null=True)
#     in_volume_rank = models.BigIntegerField(blank=True, null=True)
#     out_volume_rank = models.BigIntegerField(blank=True, null=True)
#     address_type = models.SmallIntegerField(blank=True, null=True)
#     last_transaction_datetime = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_balance_tmp_yom'
#
#
# class BitDatelist(models.Model):
#     bit_date = models.DateTimeField(blank=True, null=True)
#     update_date = models.DateTimeField(blank=True, null=True)
#     update_status = models.CharField(max_length=64, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_datelist'
#
#
# class BitErrorblocklist(models.Model):
#     id = models.BigIntegerField()
#     blockhash = models.CharField(max_length=64, blank=True, null=True)
#     next_blockhash = models.CharField(max_length=64, blank=True, null=True)
#     previous_blockhash = models.CharField(max_length=64, blank=True, null=True)
#     height = models.IntegerField(blank=True, null=True)
#     nonce = models.BigIntegerField(blank=True, null=True)
#     timestamp = models.IntegerField(blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     median_timestamp = models.IntegerField(blank=True, null=True)
#     size = models.IntegerField(blank=True, null=True)
#     stripped_size = models.IntegerField(blank=True, null=True)
#     chainwork = models.CharField(max_length=64, blank=True, null=True)
#     merkleroot = models.CharField(max_length=64, blank=True, null=True)
#     n_confirmations = models.IntegerField(blank=True, null=True)
#     difficulty = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
#     bits = models.CharField(max_length=32, blank=True, null=True)
#     version = models.IntegerField(blank=True, null=True)
#     version_hex = models.CharField(max_length=64, blank=True, null=True)
#     weight = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_errorblocklist'
#
#
# class BitExchangeRecharge(models.Model):
#     groupind = models.IntegerField()
#     trans_date = models.DateField(blank=True, null=True)
#     tot_recharge = models.DecimalField(max_digits=42, decimal_places=10, blank=True, null=True)
#     avg_recharge = models.DecimalField(max_digits=24, decimal_places=14, blank=True, null=True)
#     cnt = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_exchange_recharge'
#         unique_together = (('groupind', 'trans_date'),)
#
#
# class BitExchangeWithdraw(models.Model):
#     groupind = models.IntegerField()
#     trans_date = models.DateField(blank=True, null=True)
#     tot_withdraw = models.DecimalField(max_digits=42, decimal_places=10, blank=True, null=True)
#     avg_with_draw = models.DecimalField(max_digits=24, decimal_places=14, blank=True, null=True)
#     cnt = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_exchange_withdraw'
#         unique_together = (('groupind', 'trans_date'),)
#
#
# class BitFakeMutiinputTansaction(models.Model):
#     transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#     input_count = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_fake_mutiinput_tansaction'
#
#
# class BitFromgroupOutput(models.Model):
#     transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#     addresses = models.CharField(max_length=64, blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     output_groupind = models.IntegerField()
#     input_groupind = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_fromgroup_output'
#
#
# class BitFromgroupOutputRealtime(models.Model):
#     transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#     addresses = models.CharField(max_length=64, blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     output_groupind = models.IntegerField()
#     input_groupind = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_fromgroup_output_realtime'
#
#
# class BitIndexBalanceHis(models.Model):
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     his_date = models.DateField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_index_balance_his'
#
#
# class BitIndexHis(models.Model):
#     index_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     his_date = models.DateField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_index_his'
#
#
# class BitKnewAddress2(models.Model):
#     address = models.CharField(unique=True, max_length=64, blank=True, null=True)
#     groupind = models.IntegerField()
#     onoroff = models.IntegerField(blank=True, null=True)
#     createtime = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_knew_address2'
#
#
# class BitKnewAddress2Bak201804181002(models.Model):
#     address = models.CharField(max_length=64, blank=True, null=True)
#     groupind = models.IntegerField()
#     onoroff = models.IntegerField(blank=True, null=True)
#     createtime = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_knew_address2_bak201804181002'
#
#
# class BitMarketStat(models.Model):
#     btc_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     avg_transaction_volume_24h = models.DecimalField(db_column='avg_transaction_volume_24H', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
#     transaction_volume_24h = models.DecimalField(db_column='transaction_volume_24H', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
#     avg_transaction_count_24h = models.IntegerField(db_column='avg_transaction_count_24H', blank=True, null=True)  # Field name made lowercase.
#     btc_transaction_count_24h = models.IntegerField(db_column='btc_transaction_count_24H', blank=True, null=True)  # Field name made lowercase.
#     unconfirmed_transaction_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     unconfirmed_transaction_count = models.IntegerField(blank=True, null=True)
#     address_count = models.BigIntegerField(blank=True, null=True)
#     his_time = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_market_stat'
#
#
# class BitMarketStatHis(models.Model):
#     btc_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     avg_transaction_volume_24h = models.DecimalField(db_column='avg_transaction_volume_24H', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
#     transaction_volume_24h = models.DecimalField(db_column='transaction_volume_24H', max_digits=20, decimal_places=10, blank=True, null=True)  # Field name made lowercase.
#     avg_transaction_count_24h = models.IntegerField(db_column='avg_transaction_count_24H', blank=True, null=True)  # Field name made lowercase.
#     btc_transaction_count_24h = models.IntegerField(db_column='btc_transaction_count_24H', blank=True, null=True)  # Field name made lowercase.
#     unconfirmed_transaction_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     unconfirmed_transaction_count = models.IntegerField(blank=True, null=True)
#     address_count = models.BigIntegerField(blank=True, null=True)
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_market_stat_his'
#
#
# class BitMinerlist(models.Model):
#     address = models.CharField(max_length=64, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_minerlist'
#
#
# class BitMinerlistDistinct(models.Model):
#     address = models.CharField(max_length=64, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_minerlist_distinct'
#
#
# class BitNewFoundTransaction(models.Model):
#     transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#     groupind = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'bit_new_found_transaction'
#
#
# class BitNewKnewAddress(models.Model):
#     address = models.CharField(max_length=64, blank=True, null=True)
#     groupind = models.IntegerField(blank=True, null=True)
#     transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_new_knew_address'
#
#
# class BitOneofMutiInput(models.Model):
#     address = models.CharField(max_length=64, blank=True, null=True)
#     input_times = models.BigIntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'bit_oneof_muti_input'
#
#
# class BitReturnAnalysis(models.Model):
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     sum_in_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_out_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_count = models.IntegerField(blank=True, null=True)
#     sum_out_count = models.IntegerField(blank=True, null=True)
#     address_type = models.SmallIntegerField(blank=True, null=True)
#     last_transaction_datetime = models.DateTimeField(blank=True, null=True)
#     totreturn = models.DecimalField(max_digits=45, decimal_places=11, blank=True, null=True)
#     totinvest = models.DecimalField(max_digits=42, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_return_analysis'
#
#
# class BitRunningStatus(models.Model):
#     status = models.CharField(max_length=64, blank=True, null=True)
#     status_type = models.CharField(max_length=64, blank=True, null=True)
#     update_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_running_status'
#
#
# class BitRunningStatusHis(models.Model):
#     status = models.CharField(max_length=64, blank=True, null=True)
#     status_type = models.CharField(max_length=64, blank=True, null=True)
#     update_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_running_status_his'
#
#
# class BitTmpGroupind(models.Model):
#     groupind = models.IntegerField(blank=True, null=True)
#     knewornot = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_tmp_groupind'
#
#
# class BitTotalReturn(models.Model):
#     ret1 = models.DecimalField(max_digits=43, decimal_places=10, blank=True, null=True)
#     invest = models.DecimalField(max_digits=42, decimal_places=10, blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_total_return'
#
#
# class BitTransactionAddress(models.Model):
#     groupind = models.IntegerField(blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_transaction_address'
#
#
# class BitTransactionAddressGroupind(models.Model):
#     groupind = models.IntegerField(blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_transaction_address_groupind'
#
#
# class BitTransactionAddressGroupindRealtime(models.Model):
#     groupind = models.IntegerField(blank=True, null=True)
#     oneof_address = models.CharField(max_length=64, blank=True, null=True)
#     transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_transaction_address_groupind_realtime'
#
#
# class BitTransactionAddressRealtime(models.Model):
#     groupind = models.IntegerField(blank=True, null=True)
#     oneof_address = models.CharField(max_length=64, blank=True, null=True)
#     transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_transaction_address_realtime'
#
#
# class BitTransactionAddresscount(models.Model):
#     transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#     input_count = models.IntegerField(blank=True, null=True)
#     output_count = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bit_transaction_addresscount'
#
#
# class BitcoinBlockFile(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     filename = models.CharField(max_length=255, blank=True, null=True)
#     status = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_block_file'
#
#
# class BitcoinBlockchain(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     blockhash = models.CharField(unique=True, max_length=64, blank=True, null=True)
#     next_blockhash = models.CharField(max_length=64, blank=True, null=True)
#     previous_blockhash = models.CharField(max_length=64, blank=True, null=True)
#     height = models.IntegerField(blank=True, null=True)
#     nonce = models.BigIntegerField(blank=True, null=True)
#     timestamp = models.IntegerField(blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     median_timestamp = models.IntegerField(blank=True, null=True)
#     size = models.IntegerField(blank=True, null=True)
#     stripped_size = models.IntegerField(blank=True, null=True)
#     chainwork = models.CharField(max_length=64, blank=True, null=True)
#     merkleroot = models.CharField(max_length=64, blank=True, null=True)
#     n_confirmations = models.IntegerField(blank=True, null=True)
#     difficulty = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
#     bits = models.CharField(max_length=32, blank=True, null=True)
#     version = models.IntegerField(blank=True, null=True)
#     version_hex = models.CharField(max_length=64, blank=True, null=True)
#     weight = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_blockchain'
#
#
# class BitcoinBlockchainRealtime(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     blockhash = models.CharField(unique=True, max_length=64, blank=True, null=True)
#     next_blockhash = models.CharField(max_length=64, blank=True, null=True)
#     previous_blockhash = models.CharField(max_length=64, blank=True, null=True)
#     height = models.IntegerField(blank=True, null=True)
#     nonce = models.BigIntegerField(blank=True, null=True)
#     timestamp = models.IntegerField(blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     median_timestamp = models.IntegerField(blank=True, null=True)
#     size = models.IntegerField(blank=True, null=True)
#     stripped_size = models.IntegerField(blank=True, null=True)
#     chainwork = models.CharField(max_length=64, blank=True, null=True)
#     merkleroot = models.CharField(max_length=64, blank=True, null=True)
#     n_confirmations = models.IntegerField(blank=True, null=True)
#     difficulty = models.DecimalField(max_digits=20, decimal_places=5, blank=True, null=True)
#     bits = models.CharField(max_length=32, blank=True, null=True)
#     version = models.IntegerField(blank=True, null=True)
#     version_hex = models.CharField(max_length=64, blank=True, null=True)
#     weight = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_blockchain_realtime'
#
#
# class BitcoinCashflow(models.Model):
#     address = models.CharField(max_length=64, blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     input_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     output_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_cashflow'
#
#
# class BitcoinCashflowOutput(models.Model):
#     address = models.CharField(max_length=64, blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     input_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     output_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     miner_charge = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_cashflow_output'
#
#
# class BitcoinCashflowOutput24H(models.Model):
#     address = models.CharField(max_length=64, blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     input_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     output_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     miner_charge = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_cashflow_output_24h'
#
#
# class BitcoinCashflowOutputRealtime(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     input_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     output_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     miner_charge = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_cashflow_output_realtime'
#
#
# class BitcoinCashflowOutputSelected1(models.Model):
#     address = models.CharField(max_length=64, blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     input_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     output_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     miner_charge = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     transaction_date = models.DateField(blank=True, null=True)
#     trans_volume_doller = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_cashflow_output_selected1'
#
#
# class BitcoinCashflowOutputWinneranalyst(models.Model):
#     address = models.CharField(max_length=64, blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     input_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     output_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     miner_charge = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     transaction_date = models.DateField(blank=True, null=True)
#     trans_volume_doller = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_cashflow_output_winneranalyst'
#
#
# class BitcoinCashflowOutputWinneranalystBuyandsell(models.Model):
#     address = models.CharField(max_length=64, blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     input_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     output_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     miner_charge = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     transaction_date = models.DateField(blank=True, null=True)
#     trans_volume_doller = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     last_tran_price = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     transaction_return_rate = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_cashflow_output_winneranalyst_buyandsell'
#
#
# class BitcoinCashflowRealtime(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     input_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     output_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     miner_charge = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_cashflow_realtime'
#
#
# class BitcoinCashflowSumYom(models.Model):
#     address = models.CharField(max_length=64, blank=True, null=True)
#     trans_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     in_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     out_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     in_count = models.SmallIntegerField(blank=True, null=True)
#     out_count = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_cashflow_sum_yom'
#
#
# class BitcoinCashflowSumYom1(models.Model):
#     address = models.CharField(max_length=64, blank=True, null=True)
#     trans_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     in_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     out_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     in_count = models.SmallIntegerField(blank=True, null=True)
#     out_count = models.SmallIntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_cashflow_sum_yom_1'
#
#
# class BitcoinChartsDatas(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     price = models.FloatField(blank=True, null=True)
#     hisdate = models.DateField(unique=True, blank=True, null=True)
#     create_time = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_charts_datas'
#
#
# class BitcoinHoursChartsDatas(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     price_usd = models.FloatField(blank=True, null=True)
#     histime = models.DateTimeField(unique=True, blank=True, null=True)
#     create_time = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_hours_charts_datas'
#
#
# class BitcoinTmpBalancerank(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_tmp_balancerank'
#
#
# class BitcoinTransactionInput(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#     input_transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#     coinbase = models.CharField(max_length=128, blank=True, null=True)
#     vout = models.IntegerField(blank=True, null=True)
#     txinwitness = models.TextField(blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_transaction_input'
#
#
# class BitcoinTransactionInputRealtime(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     blockhash = models.CharField(max_length=64, blank=True, null=True)
#     transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#     input_transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#     coinbase = models.CharField(max_length=128, blank=True, null=True)
#     vout = models.IntegerField(blank=True, null=True)
#     txinwitness = models.TextField(blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_transaction_input_realtime'
#
#
# class BitcoinTransactionInputSelected1(models.Model):
#     transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     input_count = models.IntegerField(blank=True, null=True)
#     output_count = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_transaction_input_selected1'
#
#
# class BitcoinTransactionInputTmp(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#     input_transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#     coinbase = models.CharField(max_length=128, blank=True, null=True)
#     vout = models.IntegerField(blank=True, null=True)
#     txinwitness = models.TextField(blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_transaction_input_tmp'
#
#
# class BitcoinTransactionOutput(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#     value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     index = models.IntegerField(blank=True, null=True)
#     req_sigs = models.IntegerField(blank=True, null=True)
#     output_type = models.CharField(max_length=64, blank=True, null=True)
#     addresses = models.CharField(max_length=64, blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     foundinput = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_transaction_output'
#
#
# class BitcoinTransactionOutputRealtime(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     blockhash = models.CharField(max_length=64, blank=True, null=True)
#     transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#     value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     index = models.IntegerField(blank=True, null=True)
#     req_sigs = models.IntegerField(blank=True, null=True)
#     output_type = models.CharField(max_length=64, blank=True, null=True)
#     addresses = models.CharField(max_length=64, blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     foundinput = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_transaction_output_realtime'
#
#
# class BitcoinTransactionOutputRealtimeForrank(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     blockhash = models.CharField(max_length=64, blank=True, null=True)
#     transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#     value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     index = models.IntegerField(blank=True, null=True)
#     req_sigs = models.IntegerField(blank=True, null=True)
#     output_type = models.CharField(max_length=64, blank=True, null=True)
#     addresses = models.CharField(max_length=64, blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     foundinput = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_transaction_output_realtime_forrank'
#
#
# class BitcoinTransactionOutputTmp(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#     value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     index = models.IntegerField(blank=True, null=True)
#     req_sigs = models.IntegerField(blank=True, null=True)
#     output_type = models.CharField(max_length=64, blank=True, null=True)
#     addresses = models.CharField(max_length=64, blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     foundinput = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_transaction_output_tmp'
#
#
# class BitcoinTransactionOutputWithgroup(models.Model):
#     transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     groupind = models.IntegerField()
#     inputgroup = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_transaction_output_withgroup'
#
#
# class BitcoinTransactionOutputWithgroup1(models.Model):
#     transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     groupind = models.IntegerField()
#     inputgroup = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_transaction_output_withgroup1'
#
#
# class BitcoinTransactionOutputWithgroupRealtime(models.Model):
#     transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     groupind = models.IntegerField()
#     inputgroup = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_transaction_output_withgroup_realtime'
#
#
# class BitcoinUnconfirmedCashflow(models.Model):
#     address = models.CharField(max_length=64, blank=True, null=True)
#     block_time = models.DateTimeField(blank=True, null=True)
#     input_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     output_value = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     miner_charge = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_unconfirmed_cashflow'
#
#
# class BitcoinUnconfirmedTransactionsInput(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#     sequence = models.CharField(max_length=64, blank=True, null=True)
#     value = models.FloatField(blank=True, null=True)
#     addresses = models.CharField(max_length=64, blank=True, null=True)
#     hex_data = models.CharField(max_length=64, blank=True, null=True)
#     relayed_by = models.CharField(max_length=32, blank=True, null=True)
#     relayed_time = models.DateTimeField(blank=True, null=True)
#     scrapy_time = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_unconfirmed_transactions_input'
#         unique_together = (('transaction_uuid', 'addresses'),)
#
#
# class BitcoinUnconfirmedTransactionsOutput(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     transaction_uuid = models.CharField(max_length=64, blank=True, null=True)
#     value = models.FloatField(blank=True, null=True)
#     addresses = models.CharField(max_length=64, blank=True, null=True)
#     hex_data = models.CharField(max_length=64, blank=True, null=True)
#     relayed_by = models.CharField(max_length=32, blank=True, null=True)
#     relayed_time = models.DateTimeField(blank=True, null=True)
#     scrapy_time = models.DateTimeField(blank=True, null=True)
#     blockhash = models.CharField(max_length=45, blank=True, null=True)
#     output_index = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitcoin_unconfirmed_transactions_output'
#         unique_together = (('transaction_uuid', 'output_index'),)
#
#
# class BitpayAddressBlanceRank(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     balance = models.FloatField(blank=True, null=True)
#     new_balance = models.FloatField(blank=True, null=True)
#     address = models.CharField(unique=True, max_length=255, blank=True, null=True)
#     total_received = models.FloatField(blank=True, null=True)
#     total_sent = models.FloatField(blank=True, null=True)
#     last_transaction = models.CharField(max_length=255, blank=True, null=True)
#     last_block_time = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'bitpay_address_blance_rank'
#
#
# class ChangeAddressList(models.Model):
#     address = models.CharField(max_length=64, blank=True, null=True)
#     change_time = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'change_address_list'
#
#
# class CoinMarketCap(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     token = models.CharField(unique=True, max_length=255, blank=True, null=True)
#     token_name = models.CharField(max_length=255, blank=True, null=True)
#     full_name = models.CharField(max_length=255, blank=True, null=True)
#     simple_introduction = models.TextField(blank=True, null=True)
#     all_introduction = models.TextField(blank=True, null=True)
#     publish_volume = models.CharField(max_length=255, blank=True, null=True)
#     circulate_volume = models.CharField(max_length=255, blank=True, null=True)
#     official_website = models.CharField(max_length=255, blank=True, null=True)
#     white_paper = models.CharField(max_length=255, blank=True, null=True)
#     block_query = models.CharField(max_length=255, blank=True, null=True)
#     crowdfunding_price = models.CharField(max_length=255, blank=True, null=True)
#     price_usd = models.FloatField(blank=True, null=True)
#     usd_value = models.FloatField(blank=True, null=True)
#     price_btc = models.FloatField(blank=True, null=True)
#     publish_date = models.DateField(blank=True, null=True)
#     google_trend = models.TextField(blank=True, null=True)
#     simple_introduction_json = models.TextField(blank=True, null=True)
#     all_introduction_json = models.TextField(blank=True, null=True)
#     create_time = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'coin_market_cap'
#
#
# class Goodaddress(models.Model):
#     address1 = models.CharField(max_length=64, blank=True, null=True)
#     address2 = models.CharField(max_length=64, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'goodaddress'
#
#
# class Goodaddress1(models.Model):
#     address1 = models.CharField(max_length=64, blank=True, null=True)
#     address2 = models.CharField(max_length=64, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'goodaddress1'
#
#
# class GroupCount(models.Model):
#     cnt = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'group_count'
#
#
# class LitecoinChartsDatas(models.Model):
#     id = models.BigIntegerField(primary_key=True)
#     price_usd = models.FloatField(blank=True, null=True)
#     price_btc = models.FloatField(blank=True, null=True)
#     hisdate = models.DateField(unique=True, blank=True, null=True)
#     create_time = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'litecoin_charts_datas'
#
#
# class TBit24InvolumeRank1000His(models.Model):
#     ranking = models.IntegerField()
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24h_trans_volume = models.DecimalField(db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_7d_trans_volume = models.DecimalField(db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_trans_volume = models.DecimalField(db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     unconfirmed_trans_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_24involume_rank1000_his'
#
#
# class TBit24InvolumeRank1000Newrank(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24h_trans_volume = models.DecimalField(db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_7d_trans_volume = models.DecimalField(db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_trans_volume = models.DecimalField(db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     unconfirmed_trans_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_24involume_rank1000_newrank'
#
#
# class TBit24InvolumeRank1000Now(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24h_trans_volume = models.DecimalField(db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_7d_trans_volume = models.DecimalField(db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_trans_volume = models.DecimalField(db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     unconfirmed_trans_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_24involume_rank1000_now'
#
#
# class TBit24InvolumeRank1000Yom(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24h_trans_volume = models.DecimalField(db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_7d_trans_volume = models.DecimalField(db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_trans_volume = models.DecimalField(db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     unconfirmed_trans_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_24involume_rank1000_yom'
#
#
# class TBit24OutvolumeRank1000His(models.Model):
#     ranking = models.IntegerField()
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24h_trans_volume = models.DecimalField(db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_7d_trans_volume = models.DecimalField(db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_trans_volume = models.DecimalField(db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     unconfirmed_trans_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_24outvolume_rank1000_his'
#
#
# class TBit24OutvolumeRank1000Newrank(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24h_trans_volume = models.DecimalField(db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_7d_trans_volume = models.DecimalField(db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_trans_volume = models.DecimalField(db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     unconfirmed_trans_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_24outvolume_rank1000_newrank'
#
#
# class TBit24OutvolumeRank1000Now(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24h_trans_volume = models.DecimalField(db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_7d_trans_volume = models.DecimalField(db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_trans_volume = models.DecimalField(db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     unconfirmed_trans_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_24outvolume_rank1000_now'
#
#
# class TBit24OutvolumeRank1000Yom(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24h_trans_volume = models.DecimalField(db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_7d_trans_volume = models.DecimalField(db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_trans_volume = models.DecimalField(db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     unconfirmed_trans_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_24outvolume_rank1000_yom'
#
#
# class TBitBalanceRank1000His(models.Model):
#     ranking = models.IntegerField(blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     yesterday_balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_7d_balance = models.DecimalField(db_column='7d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_balance = models.DecimalField(db_column='30d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_180d_balance = models.DecimalField(db_column='180d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_365d_balance = models.DecimalField(db_column='365d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_balance_rank1000_his'
#
#
# class TBitBalanceRank1000Newrank(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     yesterday_balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_7d_balance = models.DecimalField(db_column='7d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_balance = models.DecimalField(db_column='30d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_180d_balance = models.DecimalField(db_column='180d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_365d_balance = models.DecimalField(db_column='365d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_balance_rank1000_newrank'
#
#
# class TBitBalanceRank1000Now(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     yesterday_balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_7d_balance = models.DecimalField(db_column='7d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_balance = models.DecimalField(db_column='30d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_180d_balance = models.DecimalField(db_column='180d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_365d_balance = models.DecimalField(db_column='365d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_balance_rank1000_now'
#
#
# class TBitBalanceRank1000Realtime(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     yesterday_balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_7d_balance = models.DecimalField(db_column='7d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_balance = models.DecimalField(db_column='30d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_180d_balance = models.DecimalField(db_column='180d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_365d_balance = models.DecimalField(db_column='365d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_balance_rank1000_realtime'
#
#
# class TBitBalanceRank1000Yom(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     yesterday_balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_7d_balance = models.DecimalField(db_column='7d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_balance = models.DecimalField(db_column='30d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_180d_balance = models.DecimalField(db_column='180d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_365d_balance = models.DecimalField(db_column='365d_balance', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_balance_rank1000_yom'
#
#
# class TBitBalancechangeRank1000His(models.Model):
#     ranking = models.IntegerField(blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24h_balancechange = models.DecimalField(db_column='24h_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_7d_balancechange = models.DecimalField(db_column='7d_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_balancechange = models.DecimalField(db_column='30d_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     unconfirmed_balancechange = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_balancechange_rank1000_his'
#
#
# class TBitBalancechangeRank1000Newrank(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24h_balancechange = models.DecimalField(db_column='24h_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_7d_balancechange = models.DecimalField(db_column='7d_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_balancechange = models.DecimalField(db_column='30d_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     unconfirmed_balancechange = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_balancechange_rank1000_newrank'
#
#
# class TBitBalancechangeRank1000Now(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24h_balancechange = models.DecimalField(db_column='24h_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_7d_balancechange = models.DecimalField(db_column='7d_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_balancechange = models.DecimalField(db_column='30d_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     unconfirmed_balancechange = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_balancechange_rank1000_now'
#
#
# class TBitBalancechangeRank1000Yom(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24h_balancechange = models.DecimalField(db_column='24h_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_7d_balancechange = models.DecimalField(db_column='7d_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_balancechange = models.DecimalField(db_column='30d_balancechange', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     unconfirmed_balancechange = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_balancechange_rank1000_yom'
#
#
# class TBitBalancetransRankHis(models.Model):
#     ranking = models.IntegerField(blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     transaction_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     transaction_count = models.IntegerField(blank=True, null=True)
#     last_transaction_datetime = models.DateTimeField(blank=True, null=True)
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_balancetrans_rank_his'
#
#
# class TBitBalancetransRankNewrank(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     transaction_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     transaction_count = models.IntegerField(blank=True, null=True)
#     last_transaction_datetime = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_balancetrans_rank_newrank'
#
#
# class TBitBalancetransRankNow(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     transaction_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     transaction_count = models.IntegerField(blank=True, null=True)
#     last_transaction_datetime = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_balancetrans_rank_now'
#
#
# class TBitBalancetransRankYom(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     transaction_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     transaction_count = models.IntegerField(blank=True, null=True)
#     last_transaction_datetime = models.DateTimeField(blank=True, null=True)
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_balancetrans_rank_yom'
#
#
# class TBitIncountRank1000His(models.Model):
#     ranking = models.IntegerField(blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_incount_rank1000_his'
#
#
# class TBitIncountRank1000Newrank(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_incount_rank1000_newrank'
#
#
# class TBitIncountRank1000Now(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_incount_rank1000_now'
#
#
# class TBitIncountRank1000Yom(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_incount_rank1000_yom'
#
#
# class TBitLongtermIndex(models.Model):
#     address = models.CharField(max_length=64, blank=True, null=True)
#     weight = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     start_date = models.DateField(blank=True, null=True)
#     end_date = models.DateField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_longterm_index'
#
#
# class TBitNotransRank1000His(models.Model):
#     ranking = models.IntegerField(blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     last_transaction_datetime = models.DateTimeField(blank=True, null=True)
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_notrans_rank1000_his'
#
#
# class TBitNotransRank1000Now(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     last_transaction_datetime = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_notrans_rank1000_now'
#
#
# class TBitNotransRank1000Yom(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     last_transaction_datetime = models.DateTimeField(blank=True, null=True)
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_notrans_rank1000_yom'
#
#
# class TBitOutcountRank1000His(models.Model):
#     ranking = models.IntegerField(blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_outcount_rank1000_his'
#
#
# class TBitOutcountRank1000Newrank(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_outcount_rank1000_newrank'
#
#
# class TBitOutcountRank1000Now(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_outcount_rank1000_now'
#
#
# class TBitOutcountRank1000Yom(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_outcount_rank1000_yom'
#
#
# class TBitSpecialAddress(models.Model):
#     address = models.CharField(max_length=64, blank=True, null=True)
#     address_type = models.IntegerField(blank=True, null=True)
#     start_date = models.DateField(blank=True, null=True)
#     end_date = models.DateField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_special_address'
#
#
# class TBitSumIncountRank1000His(models.Model):
#     ranking = models.IntegerField(blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_out_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_transcount = models.IntegerField(blank=True, null=True)
#     sum_out_transcount = models.IntegerField(blank=True, null=True)
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_sum_incount_rank1000_his'
#
#
# class TBitSumIncountRank1000Newrank(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_out_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_transcount = models.IntegerField(blank=True, null=True)
#     sum_out_transcount = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_sum_incount_rank1000_newrank'
#
#
# class TBitSumIncountRank1000Now(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_out_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_transcount = models.IntegerField(blank=True, null=True)
#     sum_out_transcount = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_sum_incount_rank1000_now'
#
#
# class TBitSumIncountRank1000Yom(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_out_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_transcount = models.IntegerField(blank=True, null=True)
#     sum_out_transcount = models.IntegerField(blank=True, null=True)
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_sum_incount_rank1000_yom'
#
#
# class TBitSumInvolumeRank1000His(models.Model):
#     ranking = models.IntegerField(blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_out_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_transcount = models.IntegerField(blank=True, null=True)
#     sum_out_transcount = models.IntegerField(blank=True, null=True)
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_sum_involume_rank1000_his'
#
#
# class TBitSumInvolumeRank1000Newrank(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_out_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_transcount = models.IntegerField(blank=True, null=True)
#     sum_out_transcount = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_sum_involume_rank1000_newrank'
#
#
# class TBitSumInvolumeRank1000Now(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_out_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_transcount = models.IntegerField(blank=True, null=True)
#     sum_out_transcount = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_sum_involume_rank1000_now'
#
#
# class TBitSumInvolumeRank1000Yom(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_out_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_transcount = models.IntegerField(blank=True, null=True)
#     sum_out_transcount = models.IntegerField(blank=True, null=True)
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_sum_involume_rank1000_yom'
#
#
# class TBitSumOutcountRank1000His(models.Model):
#     ranking = models.IntegerField(blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_out_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_transcount = models.IntegerField(blank=True, null=True)
#     sum_out_transcount = models.IntegerField(blank=True, null=True)
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_sum_outcount_rank1000_his'
#
#
# class TBitSumOutcountRank1000Newrank(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_out_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_transcount = models.IntegerField(blank=True, null=True)
#     sum_out_transcount = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_sum_outcount_rank1000_newrank'
#
#
# class TBitSumOutcountRank1000Now(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_out_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_transcount = models.IntegerField(blank=True, null=True)
#     sum_out_transcount = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_sum_outcount_rank1000_now'
#
#
# class TBitSumOutcountRank1000Yom(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_out_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_transcount = models.IntegerField(blank=True, null=True)
#     sum_out_transcount = models.IntegerField(blank=True, null=True)
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_sum_outcount_rank1000_yom'
#
#
# class TBitSumOutvolumeRank1000His(models.Model):
#     ranking = models.IntegerField(blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_out_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_transcount = models.IntegerField(blank=True, null=True)
#     sum_out_transcount = models.IntegerField(blank=True, null=True)
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_sum_outvolume_rank1000_his'
#
#
# class TBitSumOutvolumeRank1000Newrank(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_out_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_transcount = models.IntegerField(blank=True, null=True)
#     sum_out_transcount = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_sum_outvolume_rank1000_newrank'
#
#
# class TBitSumOutvolumeRank1000Now(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_out_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_transcount = models.IntegerField(blank=True, null=True)
#     sum_out_transcount = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_sum_outvolume_rank1000_now'
#
#
# class TBitSumOutvolumeRank1000Yom(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_out_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     sum_in_transcount = models.IntegerField(blank=True, null=True)
#     sum_out_transcount = models.IntegerField(blank=True, null=True)
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_sum_outvolume_rank1000_yom'
#
#
# class TBitTransactionVolume10Minute(models.Model):
#     transaction_time = models.DateTimeField(primary_key=True)
#     volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     miner_income = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     miner_charge = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_transaction_volume_10minute'
#
#
# class TBitTransactionVolumeDay(models.Model):
#     transaction_date = models.DateTimeField(primary_key=True)
#     volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     miner_income = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     miner_charge = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_transaction_volume_day'
#
#
# class TBitTranscountRank1000His(models.Model):
#     ranking = models.IntegerField(blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24h_transaction_count = models.IntegerField(db_column='24h_transaction_count', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_7d_transaction_count = models.IntegerField(db_column='7d_transaction_count', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_transaction_count = models.IntegerField(db_column='30d_transaction_count', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     unconfirmed_transaction_count = models.IntegerField(blank=True, null=True)
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_transcount_rank1000_his'
#
#
# class TBitTranscountRank1000Newrank(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24h_transaction_count = models.IntegerField(db_column='24h_transaction_count', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_7d_transaction_count = models.IntegerField(db_column='7d_transaction_count', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_transaction_count = models.IntegerField(db_column='30d_transaction_count', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     unconfirmed_transaction_count = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_transcount_rank1000_newrank'
#
#
# class TBitTranscountRank1000Now(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24h_transaction_count = models.IntegerField(db_column='24h_transaction_count', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_7d_transaction_count = models.IntegerField(db_column='7d_transaction_count', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_transaction_count = models.IntegerField(db_column='30d_transaction_count', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     unconfirmed_transaction_count = models.IntegerField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_transcount_rank1000_now'
#
#
# class TBitTranscountRank1000Yom(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24h_transaction_count = models.IntegerField(db_column='24h_transaction_count', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_7d_transaction_count = models.IntegerField(db_column='7d_transaction_count', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_transaction_count = models.IntegerField(db_column='30d_transaction_count', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     unconfirmed_transaction_count = models.IntegerField(blank=True, null=True)
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_transcount_rank1000_yom'
#
#
# class TBitTransvolumeRank1000His(models.Model):
#     ranking = models.IntegerField(blank=True, null=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24h_trans_volume = models.DecimalField(db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_7d_trans_volume = models.DecimalField(db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_trans_volume = models.DecimalField(db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     unconfirmed_trans_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_transvolume_rank1000_his'
#
#
# class TBitTransvolumeRank1000Newrank(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24h_trans_volume = models.DecimalField(db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_7d_trans_volume = models.DecimalField(db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_trans_volume = models.DecimalField(db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     unconfirmed_trans_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_transvolume_rank1000_newrank'
#
#
# class TBitTransvolumeRank1000Now(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24h_trans_volume = models.DecimalField(db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_7d_trans_volume = models.DecimalField(db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_trans_volume = models.DecimalField(db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     unconfirmed_trans_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_transvolume_rank1000_now'
#
#
# class TBitTransvolumeRank1000Yom(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     number_24_in_volume = models.DecimalField(db_column='24_in_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_volume = models.DecimalField(db_column='24_out_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_in_transcount = models.IntegerField(db_column='24_in_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24_out_transcount = models.IntegerField(db_column='24_out_transcount', blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_24h_trans_volume = models.DecimalField(db_column='24h_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_7d_trans_volume = models.DecimalField(db_column='7d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     number_30d_trans_volume = models.DecimalField(db_column='30d_trans_volume', max_digits=20, decimal_places=10, blank=True, null=True)  # Field renamed because it wasn't a valid Python identifier.
#     unconfirmed_trans_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     his_date = models.DateTimeField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_transvolume_rank1000_yom'
#
#
# class TBitUnconfirmedRank1000Now(models.Model):
#     ranking = models.AutoField(primary_key=True)
#     address = models.CharField(max_length=64, blank=True, null=True)
#     balance = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     unconfirmed_transaction_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     unconfirmed_in_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     unconfirmed_out_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#     transaction_volume = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 't_bit_unconfirmed_rank1000_now'
#
#
# class Tmp1(models.Model):
#     groupind = models.IntegerField()
#
#     class Meta:
#         managed = False
#         db_table = 'tmp1'
#
#
# class TmpMaxblocktimeTest(models.Model):
#     max_block_time_field = models.DateTimeField(db_column='max(block_time)', blank=True, null=True)  # Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
#
#     class Meta:
#         managed = False
#         db_table = 'tmp_maxblocktime_test'
