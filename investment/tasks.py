# coding: utf-8
'''
Created on 2018年3月23日

@author: likun
'''
from django.db import connections
from celery import task
from common.decorators import debug_time
import datetime
from random import randint

import pygal
from django.conf import settings
from django.db.models.aggregates import Sum, Count
from blockchain_db.models import BitMinerlist, BitKnewAddress2
from blockchain_db.models import BitcoinChartsDatas, TBitSpecialAddress,\
    BitExchangeRecharge, BitExchangeWithdraw, TBitBalanceRank1000His
from common.utils import coin_name, send_mail_files
from common.models_ltc_db import TLiteSpecialAddress,\
    LiteStockCashflow, LiteExchangeRecharge, LiteExchangeWithdraw,\
    LitecoinChartsDatas, TLiteBalanceRank1000His, LiteMinerlist,\
    LiteKnewAddress2


@debug_time
def build_data():
    start = datetime.date(2013, 4, 28)
    end = datetime.date(2018, 3, 14)
    data = []
    days = 0
    for _ in range((end - start).days):
        days += 1
        print days
        data.append(LiteStockCashflow(address_type=1, his_date=start + datetime.timedelta(
            days=days), in_amount=randint(1000, 10000), out_amount=randint(1000, 10000)))
        data.append(LiteStockCashflow(address_type=2, his_date=start + datetime.timedelta(
            days=days), in_amount=randint(300, 1000), out_amount=randint(300, 1000)))
        data.append(LiteStockCashflow(address_type=3, his_date=start + datetime.timedelta(
            days=days), in_amount=randint(0, 300), out_amount=randint(0, 300)))
    LiteStockCashflow.objects.using('ltc').bulk_create(data)


@task
@debug_time
def build_image_temp(coin, start, end, email):
    # 近期行情
    if coin == 'BTC':
        hq = BitcoinChartsDatas.objects.using('btc').order_by('hisdate')
    else:
        hq = LitecoinChartsDatas.objects.using('ltc').order_by('hisdate')
    hq = hq.filter(hisdate__gte=start, hisdate__lte=end)
    hq_date = map(lambda x: x.hisdate, hq)
    if coin == 'BTC':
        hq_data = map(lambda x: x.price, hq)
    else:
        hq_data = map(lambda x: x.price_usd, hq)

    custom_css = '''
              {{ id }}.title {
                font-family: Songti;
              }
              {{ id }}text {
                font-family: Songti;
              }
              {{ id }}.legends .legend text {
                font-family: Songti;
              }
              {{ id }}.axis text {
                font-family: Songti;
              }
              {{ id }}.axis.y text {
                font-family: Songti;
              }
              {{ id }}#tooltip text {
                font-family: Songti;
              }
              '''
    custom_css_file = '/tmp/pygal_temp_custom_style.css'
    with open(custom_css_file, 'w') as f:
        f.write(custom_css)

    config = pygal.Config()
    config.css.append('file://' + custom_css_file)
    config.x_value_formatter = lambda x: x.strftime('%-m/%-d')

    hq_chart = pygal.Line(config, title=u'{}行情'.format(coin_name(coin)))
    hq_chart.x_labels = hq_date
    hq_chart.add('', hq_data)
    hq_path = u'{}chart/{}_hq_{}_{}.png'.format(
        settings.MEDIA_ROOT, coin, start, end)
    hq_chart.render_to_png(hq_path)

    # 账户买卖比例
    if coin == 'BTC':
        qs1 = TBitSpecialAddress.objects.using(
            'btc').filter(address_type=1).only('address')
        qs2 = TBitSpecialAddress.objects.using(
            'btc').filter(address_type=2).only('address')
        table = 'blockchain_db.bitcoin_cashflow_output'
        cursor = connections['btc'].cursor()

    else:
        qs1 = TLiteSpecialAddress.objects.using(
            'ltc').filter(address_type=1).only('address')
        qs2 = TLiteSpecialAddress.objects.using(
            'ltc').filter(address_type=2).only('address')
        table = 'ltc_db.litecoin_cashflow_output'
        cursor = connections['ltc'].cursor()

    addresses1 = map(lambda x: x.address, qs1)
    addresses2 = map(lambda x: x.address, qs2)

    sell_sql = '''
        SELECT
            count(*)
        FROM
            {0}
        WHERE
            (output_value - input_value) < 0
        AND address IN %s
        AND block_time > %s
        AND block_time < %s
        ORDER BY
            block_time DESC
        
    '''.format(table)
    buy_sql = '''
        SELECT
            count(*)
        FROM
            {0}
        WHERE
            (output_value - input_value) > 0
        AND address IN %s
        AND block_time > %s
        AND block_time < %s
        ORDER BY
            block_time DESC
    '''.format(table)

    cursor.execute(
        sell_sql, [tuple(addresses1), start, end])
    sell1 = cursor.fetchone()[0]

    cursor.execute(
        sell_sql, [tuple(addresses2), start, end])
    sell2 = cursor.fetchone()[0]

    cursor.execute(
        buy_sql, [tuple(addresses1), start, end])
    buy1 = cursor.fetchone()[0]

    cursor.execute(
        buy_sql, [tuple(addresses2), start, end])
    buy2 = cursor.fetchone()[0]

    bar_chart = pygal.HorizontalStackedBar(
        config, print_values=True, title=u'聪明账户与韭菜账户买卖比例')
    bar_chart.x_labels = ('', u'聪明账户', u'韭菜账户',  '')
    if buy1 and buy2:
        bar_chart.add(
            u'买', (buy1 / (sell1 + buy1), buy2 / (sell2 + buy2)))
        bar_chart.add(
            u'卖', (sell1 / (sell1 + buy1), sell2 / (sell2 + buy2)))

    bar_chart_path = u'{}chart/{}_bar_{}_{}.png'.format(
        settings.MEDIA_ROOT, coin, start, end)
    bar_chart.render_to_png(bar_chart_path)

    # 前5大交易所充值提现
    if coin == 'BTC':
        top5 = [19, 124, 84, 107, 602]
        recharge = BitExchangeRecharge.objects.using('btc').filter(groupind__in=top5, trans_date__gte=start, trans_date__lte=end)\
            .values('trans_date').annotate(sum_recharge=Sum('tot_recharge')).order_by('trans_date')
        withdraw = BitExchangeWithdraw.objects.using('btc').filter(groupind__in=top5, trans_date__gte=start, trans_date__lte=end)\
            .values('trans_date').annotate(sum_withdraw=Sum('tot_withdraw')).order_by('trans_date')
    else:
        top5 = [21, 1, 110, 101, 28]
        recharge = LiteExchangeRecharge.objects.using('ltc').filter(groupind__in=top5, trans_date__gte=start, trans_date__lte=end)\
            .values('trans_date').annotate(sum_recharge=Sum('tot_recharge')).order_by('trans_date')
        withdraw = LiteExchangeWithdraw.objects.using('ltc').filter(groupind__in=top5, trans_date__gte=start, trans_date__lte=end)\
            .values('trans_date').annotate(sum_withdraw=Sum('tot_withdraw')).order_by('trans_date')
    recharge_data = map(lambda x: x.get('sum_recharge'), recharge)
    x_labels = map(lambda x: x.get('trans_date'), recharge)
    withdraw_data = map(lambda x: x.get('sum_withdraw'), withdraw)

    tran_chart = pygal.Line(config, title=u'前5大交易所充值提现')
    tran_chart.x_labels = x_labels
    tran_chart.add(u'充值', recharge_data)
    tran_chart.add(u'提现', withdraw_data)
    tran_chart_path = u'{}chart/{}_tran_{}_{}.png'.format(
        settings.MEDIA_ROOT, coin, start, end)
    tran_chart.render_to_png(tran_chart_path)

    # 前1000持仓变化

    if coin == 'BTC':
        qs = TBitBalanceRank1000His.objects.using('btc').filter(his_date__gte=start, his_date__lte=end)\
            .values('his_date').annotate(sum_balance=Sum('balance')).order_by('his_date')
        address_qs = TBitBalanceRank1000His.objects.using('btc').filter(his_date__gte=start, his_date__lte=end)\
            .values('address').annotate(count=Count('address')).order_by('address')
        addresses = set(map(lambda x: x.get('address'), address_qs))
        org_qs = BitKnewAddress2.objects.using(
            'btc').filter(onoroff=1, address__in=addresses)
        org_address = map(lambda x: x.address, org_qs)
        org_exclude_qs = TBitBalanceRank1000His.objects.using('btc').filter(his_date__gte=start, his_date__lte=end).exclude(address__in=org_address)\
            .values('his_date').annotate(sum_balance=Sum('balance')).order_by('his_date')
    else:
        qs = TLiteBalanceRank1000His.objects.using('ltc').filter(his_date__gte=start, his_date__lte=end)\
            .values('his_date').annotate(sum_balance=Sum('balance')).order_by('his_date')

        address_qs = TLiteBalanceRank1000His.objects.using('ltc').filter(his_date__gte=start, his_date__lte=end)\
            .values('address').annotate(count=Count('address')).order_by('address')
        addresses = set(map(lambda x: x.get('address'), address_qs))
        org_qs = LiteKnewAddress2.objects.using(
            'ltc').filter(onoroff=1, address__in=addresses)
        org_address = map(lambda x: x.address, org_qs)
        org_exclude_qs = TLiteBalanceRank1000His.objects.using('ltc').filter(his_date__gte=start, his_date__lte=end).exclude(address__in=org_address)\
            .values('his_date').annotate(sum_balance=Sum('balance')).order_by('his_date')

    hold_data = map(lambda x: x.get('sum_balance'), qs)
    org_exclude_hold_data = map(
        lambda x: x.get('sum_balance'), org_exclude_qs)
    x_labels = map(lambda x: x.get('his_date'), qs)

    hold_chart = pygal.StackedLine(config, fill=True, title=u'前1000地址累计持仓')
    hold_chart.x_labels = x_labels
    hold_chart.add(u'前1000持仓', hold_data)
    hold_chart.add(u'前1000(排除交易所)', org_exclude_hold_data)
    hold_chart_path = u'{}chart/{}_hold_{}_{}.png'.format(
        settings.MEDIA_ROOT, coin, start, end)
    hold_chart.render_to_png(hold_chart_path)

    # 用户类型持仓
    if coin == 'BTC':
        all_balance = TBitBalanceRank1000His.objects.using('btc').filter(his_date__gte=start, his_date__lte=end)\
            .aggregate(sum_balance=Sum('balance')).get('sum_balance')
        address_qs = TBitBalanceRank1000His.objects.using('btc').filter(his_date__gte=start, his_date__lte=end)\
            .values('address').annotate(count=Count('address')).order_by('address')
        addresses = set(map(lambda x: x.get('address'), address_qs))
        miner_qs = BitMinerlist.objects.using(
            'btc').filter(address__in=addresses)
        miner_address = map(lambda x: x.address, miner_qs)
        org_qs = BitKnewAddress2.objects.using(
            'btc').filter(onoroff=1, address__in=addresses)
        org_address = map(lambda x: x.address, org_qs)
        org_balance = TBitBalanceRank1000His.objects.using('btc').filter(his_date__gte=start, his_date__lte=end).filter(address__in=org_address)\
            .aggregate(sum_balance=Sum('balance')).get('sum_balance', 0)
        miner_balance = TBitBalanceRank1000His.objects.using('btc').filter(his_date__gte=start, his_date__lte=end).filter(address__in=miner_address)\
            .aggregate(sum_balance=Sum('balance')).get('sum_balance', 0)
    else:
        all_balance = TLiteBalanceRank1000His.objects.using('ltc').filter(his_date__gte=start, his_date__lte=end)\
            .aggregate(sum_balance=Sum('balance')).get('sum_balance')
        address_qs = TLiteBalanceRank1000His.objects.using('ltc').filter(his_date__gte=start, his_date__lte=end)\
            .values('address').annotate(count=Count('address')).order_by('address')
        addresses = set(map(lambda x: x.get('address'), address_qs))
        miner_qs = LiteMinerlist.objects.using(
            'ltc').filter(address__in=addresses)

        miner_address = map(lambda x: x.address, miner_qs)
        org_qs = LiteKnewAddress2.objects.using(
            'ltc').filter(onoroff=1, address__in=addresses)
        org_address = map(lambda x: x.address, org_qs)
        org_balance = TLiteBalanceRank1000His.objects.using('ltc').filter(his_date__gte=start, his_date__lte=end).filter(address__in=org_address)\
            .aggregate(sum_balance=Sum('balance')).get('sum_balance', 0)
        miner_balance = TLiteBalanceRank1000His.objects.using('ltc').filter(his_date__gte=start, his_date__lte=end).filter(address__in=miner_address)\
            .aggregate(sum_balance=Sum('balance')).get('sum_balance', 0)

    pie_chart = pygal.Pie(config, print_values=True, title=u'用户类型持仓占比')
    pie_chart.value_formatter = lambda x: '{:.2%}'.format(x)
    if all_balance:
        org_data = org_balance / all_balance
        miner_data = miner_balance / all_balance
        pie_chart.add(u'交易所',  org_data)
        pie_chart.add(u'矿机', miner_data)
        pie_chart.add(u'其他', 1 - org_data - miner_data)
    pie_chart_path = u'{}chart/{}_pie_{}_{}.png'.format(
        settings.MEDIA_ROOT, coin, start, end)
    pie_chart.render_to_png(pie_chart_path)

    send_mail_files(u'{}至{}{}模版'.format(
        start, end, coin_name(coin)), [email, ], [hq_path, bar_chart_path,
                                                  tran_chart_path, hold_chart_path, pie_chart_path])
