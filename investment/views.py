# coding: utf-8
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now

from common.rest_utils import app_user, app_data_required, app_member_required,\
    data_bad_response

import datetime
from rest_framework.views import APIView
from common.utils import datetime2microsecond, avg, hide_address
from common.models_ltc_db import IndexHis, TLiteSpecialAddress,\
    LiteStockCashflow, LiteExchangeRecharge, LiteExchangeWithdraw,\
    LitecoinChartsDatas
from usercenter.models import Subscribe
from collections import OrderedDict
from django.db import connections
from blockchain_db.models import BitcoinChartsDatas, TBitSpecialAddress,\
    BitExchangeRecharge, BitExchangeWithdraw


MICROSECONDDAY = 86400000


def get_date_range():
    hq = LitecoinChartsDatas.objects.using('ltc').order_by('hisdate')
    start = hq.first().hisdate
    end = hq.last().hisdate
    return datetime2microsecond(start), datetime2microsecond(end)


def fill_data(data):
    start, end = get_date_range()
    if start < data[0][0]:
        index = 0
        for day in range(start, data[0][0], MICROSECONDDAY):
            data.insert(index, (day, None))
            index += 1
    if end > data[-1][0]:
        for day in range(data[-1][0] + MICROSECONDDAY, end, MICROSECONDDAY):
            data.append((day, None))
        data.append((end, None))

    for i in range(0, len(data)):
        if i < len(data) - 1 and data[i + 1][0] - data[i][0] != MICROSECONDDAY:
            data.insert(i + 1, (data[i][0] + MICROSECONDDAY, 0))

    return start, end


class QuotationListAPIView(APIView):
    '''
    行情指数
    '''

    def get(self, request, *args, **kwargs):
        data = request.query_params.copy()
        coin = data.get('coin', 'LTC')
        user = app_user(request)
        if coin == 'BTC':
            hq = BitcoinChartsDatas.objects.using('btc').order_by('hisdate')
        else:
            hq = LitecoinChartsDatas.objects.using('ltc').order_by('hisdate')

        if not (user and user.is_member):
            hq = hq.filter(hisdate__lt=now() - datetime.timedelta(days=7))

        if coin == 'BTC':
            data = map(lambda x: (datetime2microsecond(
                x.hisdate), x.price), hq)
        else:
            data = map(lambda x: (datetime2microsecond(
                x.hisdate), x.price_usd), hq)
        start, end = fill_data(data)
        return Response({'data': data, 'start': start, 'end': end})


class PositionListAPIView(APIView):
    '''
    持仓指数
    '''

    def get(self, request, *args, **kwargs):
        user = app_user(request)
        data = request.query_params.copy()
        coin = data.get('coin', 'LTC')
        if coin == 'BTC':
            qs = IndexHis.objects.using('btc').order_by('his_date')
        else:
            qs = IndexHis.objects.using('ltc').order_by('his_date')

        if not (user and user.is_member):
            qs = qs.filter(his_date__lt=now() - datetime.timedelta(days=7))
        data = map(lambda x: (datetime2microsecond(x.his_date), x.index_value
                              ), qs)
        start, end = fill_data(data)

        return Response({'data': data, 'start': start, 'end': end})


class PositionWarningSubscribeAPIView(APIView):
    '''
    持仓预警订阅
    status :1: 订阅 0: 取消
    '''
    @app_member_required
    def post(self, request, *args, **kwargs):
        user = request.app_user
        data = request.data
        status = data.get('status', '1')
        coin = data.get('coin', 'LTC')
        Subscribe.objects.update_or_create(category='position',
                                           user=user, coin_type=coin, defaults={'status': status})
        return Response({'code': 0, 'detail': _(u'订阅成功') if status == '1' else _(u'取消成功')})


class TransactionAPIView(APIView):
    '''
    交易行情
    address_type 1: 优秀账户；2: 韭菜账户
    '''

    def get(self, request, *args, **kwargs):
        user = app_user(request)
        data = request.query_params.copy()
        address_type = data.get('address_type', '1')
        coin = data.get('coin', 'LTC')
        hq_data = OrderedDict()

        if coin == 'BTC':
            hq = BitcoinChartsDatas.objects.using('btc').order_by('hisdate')
            qs = TBitSpecialAddress.objects.using(
                'btc').filter(address_type=address_type).only('address')
            table = 'blockchain_db.bitcoin_cashflow_output'
            cursor = connections['btc'].cursor()
            map(lambda x: hq_data.update(
                {datetime2microsecond(x.hisdate): x.price}), hq)
        else:
            hq = LitecoinChartsDatas.objects.using('ltc').order_by('hisdate')
            qs = TLiteSpecialAddress.objects.using(
                'ltc').filter(address_type=address_type).only('address')
            table = 'ltc_db.litecoin_cashflow_output'
            cursor = connections['ltc'].cursor()
            map(lambda x: hq_data.update(
                {datetime2microsecond(x.hisdate): x.price_usd}), hq)

        end_date = now()
        if not (user and user.is_member):
            end_date = now() - datetime.timedelta(days=7)

        addresses = map(lambda x: x.address, qs)

        sell_sql = '''
            SELECT
                address ,
                block_time ,
                input_value ,
                output_value
            FROM
                {0}
            WHERE
                (output_value - input_value) < -10
            AND address IN %s
            AND block_time < %s
            ORDER BY
                block_time DESC
            
        '''.format(table)
        buy_sql = '''
            SELECT
                address ,
                block_time ,
                input_value ,
                output_value
            FROM
                {0}
            WHERE
                (output_value - input_value) > 0
            AND address IN %s
            AND block_time < %s
            ORDER BY
                block_time DESC
        '''.format(table)

        cursor.execute(
            sell_sql, [tuple(addresses), end_date])
        sell_qs = cursor.fetchall()

        cursor.execute(
            buy_sql, [tuple(addresses), end_date])
        buy_qs = cursor.fetchall()

        buy_data = {}
        start, end = get_date_range()

        # 按地址生成买数据buy_data
        for address, block_time, input_value, output_value in buy_qs:
            buy = {'address': address, 'block_time': block_time, 'input_value': input_value,
                   'output_value': output_value, 'trans': abs(output_value - input_value)}
            _arr = buy_data.get(address, [])
            _arr.append(buy)
            buy_data.update({address: _arr})
        sell_data = {}
        buy_sell = {}
        # buy_sell买卖数据一对多
        for address, block_time, input_value, output_value in sell_qs:
            trans = abs(output_value - input_value)
            # 按地址生成生成卖数据sell_data
            sell = {'address': address, 'block_time': block_time, 'input_value': input_value,
                    'output_value': output_value, 'trans': trans}
            sell_arr = buy_data.get(address, [])
            sell_arr.append(sell)
            sell_data.update({address: sell_arr})

            _arr = buy_data.get(address, [])

            b = None
            for x in _arr:
                if x.get('block_time') < block_time and x.get('trans') > trans / 4:
                    b = x
                    break
            if b:
                points = buy_sell.get('{}{}'.format(
                    b.get('address'), b.get('block_time')), {})
                sell_arr = points.get('sell', [])

                buy_price = hq_data.get(
                    datetime2microsecond(b.get('block_time').date()))

                sell_price = hq_data.get(
                    datetime2microsecond(block_time.date()))

                profit = '{:.2%}'.format((sell_price - buy_price) / buy_price)
                address = hide_address(b.get('address'))
                sell_arr.append({'id': b.get('address'), 'address': address, 'block_time': datetime2microsecond(block_time), 'buy_price': buy_price,
                                 'sell_price': sell_price, 'profit': profit})
                points.update({'sell': sell_arr})

                buy = points.get('buy', {})
                sell_price_avg = avg(
                    map(lambda x: x.get('sell_price'), sell_arr))
                profit_avg = '{:.2%}'.format(
                    (sell_price_avg - buy_price) / buy_price)
                buy.update({'id': b.get('address'), 'address': address, 'block_time': datetime2microsecond(b.get('block_time')), 'buy_price': buy_price,
                            'sell_price': sell_price_avg, 'profit': profit_avg})
                points.update({'buy': buy})

                buy_sell.update(
                    {'{}{}'.format(b.get('address'), b.get('block_time')): points})

        only_buy = {}
        # 寻找买点之后没有卖点的数据
        for address, block_time, input_value, output_value in buy_qs:
            trans = abs(output_value - input_value)
            _arr = sell_data.get(address, [])

            s = False
            for x in _arr:
                if x.get('block_time') > block_time:
                    s = True
                    break
            if s:
                continue
            else:
                points = only_buy.get('{}{}'.format(address, block_time), {})
                buy_arr = points.get('buy', [])

                buy_price = hq_data.get(
                    datetime2microsecond(block_time.date()))

                sell_price = hq_data.values()[-1]

                profit = '{:.2%}'.format((sell_price - buy_price) / buy_price)
                buy_arr.append({'id': address, 'address': hide_address(address), 'block_time': datetime2microsecond(block_time), 'buy_price': buy_price,
                                'sell_price': sell_price, 'profit': profit})
                points.update({'buy': buy_arr})

                sell = points.get('sell', {})
                buy_price_avg = avg(
                    map(lambda x: x.get('buy_price'), buy_arr))
                profit_avg = '{:.2%}'.format(
                    (sell_price - buy_price_avg) / buy_price_avg)
                sell.update({'id': address, 'address': hide_address(address), 'block_time': hq_data.keys()[-1], 'buy_price': buy_price_avg,
                             'sell_price': sell_price, 'profit': profit_avg})
                points.update({'sell': sell})

                only_buy.update(
                    {'{}{}'.format(address, block_time): points})

        return Response({'data': buy_sell.values(), 'start': start, 'end': end, 'buy_data': only_buy.values()})


class TransactionWarningSubscribeAPIView(APIView):
    '''
    地址交易预警订阅
    status :1: 订阅 0: 取消
    '''
    @app_member_required
    @app_data_required('pk')
    def post(self, request, *args, **kwargs):
        user = request.app_user
        data = request.data
        status = data.get('status', '1')
        coin = data.get('coin', 'LTC')

        address = data.get('pk')
        Subscribe.objects.update_or_create(category='transaction',
                                           user=user, address=address, coin_type=coin, defaults={'status': status})
        return Response({'code': 0, 'detail': _(u'订阅成功') if status == '1' else _(u'取消成功')})


class ExchangeAPIView(APIView):
    '''
    交易所行情
    '''

    def get(self, request, *args, **kwargs):
        user = app_user(request)
        qs = LiteStockCashflow.objects.using('ltc').order_by('his_date')
        hq = LitecoinChartsDatas.objects.using('ltc').order_by('hisdate')
        if not (user and user.is_member):
            qs = qs.filter(his_date__lt=now() - datetime.timedelta(days=7))
            hq = hq.filter(hisdate__lt=now() - datetime.timedelta(days=7))

        qs = list(qs)

        data = {}
        map(lambda x: data.update(
            {datetime2microsecond(x.hisdate): x.price_usd}), hq)

        def in_amount(x):
            ts = datetime2microsecond(x.his_date)
            price = data.get(ts) * float(x.in_amount) if data.get(ts) else '-'
            return (ts,  x.in_amount, price)

        def out_amount(x):
            ts = datetime2microsecond(x.his_date)
            price = data.get(ts) * float(x.out_amount) if data.get(ts) else '-'
            return (ts,  x.out_amount, price)

        l_in = map(in_amount, filter(
            lambda x: x.address_type == 1, qs))

        l_out = map(out_amount, filter(
            lambda x: x.address_type == 1, qs))

        m_in = map(in_amount, filter(
            lambda x: x.address_type == 2, qs))

        m_out = map(out_amount, filter(
            lambda x: x.address_type == 2, qs))

        s_in = map(in_amount, filter(
            lambda x: x.address_type == 3, qs))

        s_out = map(out_amount, filter(
            lambda x: x.address_type == 3, qs))

        def line_data(x):
            ts = x[0][0]
            amount = float(sum([x[0][1], x[1][1], x[2][1]]))
            price = data.get(ts) * amount if data.get(ts) else '-'
            return (ts, amount, price)

        in_line = map(line_data, zip(l_in, m_in, s_in))

        out_line = map(line_data, zip(l_out, m_out, s_out))

        def bar_data(x):
            ts = datetime2microsecond(x.his_date)
            amount = float(x.in_amount - x.out_amount)
            price = data.get(ts) * amount if data.get(ts) else '-'
            return (ts, amount, price)

        l_bar = map(bar_data, filter(
            lambda x: x.address_type == 1, qs))

        m_bar = map(bar_data, filter(
            lambda x: x.address_type == 2, qs))

        s_bar = map(bar_data, filter(
            lambda x: x.address_type == 3, qs))

        bar_line = map(lambda x: (x[0][0], sum((x[0][1], x[1][1], x[2][1])), sum((
            x[0][2], x[1][2], x[2][2]))), zip(l_bar, m_bar, s_bar))
        start, end = fill_data(l_in)
        fill_data(l_out)
        fill_data(m_in)
        fill_data(m_out)
        fill_data(s_in)
        fill_data(s_out)
        fill_data(in_line)
        fill_data(out_line)
        fill_data(l_bar)
        fill_data(m_bar)
        fill_data(s_bar)
        fill_data(bar_line)
        return Response({'in_line': {'data': in_line, 'name': _(u'总流入')},
                         'out_line': {'data': out_line, 'name': _(u'总流出')},
                         'l_in': {'data': l_in, 'name': _(u'大户流入')},
                         'l_out': {'data': l_out, 'name': _(u'大户流出')},
                         'm_in': {'data': m_in, 'name': _(u'中户流入')},
                         'm_out': {'data': m_out, 'name': _(u'中户流出')},
                         's_in': {'data': s_in, 'name': _(u'小户流入')},
                         's_out': {'data': s_out, 'name': _(u'小户流出')},
                         'l_bar': {'data': l_bar, 'name': _(u'大户净流入')},
                         's_bar': {'data': s_bar, 'name': _(u'小户净流入')},
                         'm_bar': {'data': m_bar, 'name': _(u'中户净流入')},
                         'bar_line': {'data': bar_line, 'name': _(u'净流入')},
                         'start': start, 'end': end})


class ExchangeAVGAPIView(APIView):
    '''
    交易所笔均行情
    '''

    def get(self, request, *args, **kwargs):
        get_data = request.query_params.copy()
        coin = get_data.get('coin', 'LTC')
        data = OrderedDict()
        user = app_user(request)

        if coin == 'BTC':
            recharge_qs = BitExchangeRecharge.objects.using(
                'btc').filter(groupind=4).order_by('trans_date')
            withdraw_qs = BitExchangeWithdraw.objects.using(
                'btc').filter(groupind=4).order_by('trans_date')
        else:
            recharge_qs = LiteExchangeRecharge.objects.using(
                'ltc').filter(groupind=1).order_by('trans_date')
            withdraw_qs = LiteExchangeWithdraw.objects.using(
                'ltc').filter(groupind=1).order_by('trans_date')

        if not (user and user.is_member):
            recharge_qs = recharge_qs.filter(
                trans_date__lt=now() - datetime.timedelta(days=7))
            withdraw_qs = withdraw_qs.filter(
                trans_date__lt=now() - datetime.timedelta(days=7))

        if recharge_qs:
            map(lambda x: data.update({str(datetime2microsecond(x.trans_date)): {'recharge': {'tot': x.tot_recharge, 'avg': x.avg_recharge}}}),
                recharge_qs)

            for obj in withdraw_qs:
                key = str(datetime2microsecond(obj.trans_date))
                withdraw = data.get(key)
                if withdraw:
                    withdraw.update(
                        {'withdraw': {'tot': obj.tot_withdraw, 'avg': obj.avg_with_draw}})
            withdraw_line, recharge_line, in_bar, out_bar, net_bar = [], [], [], [], []
            for day, v in data.items():
                day = int(day)
                withdraw = v.get('withdraw')
                recharge = v.get('recharge')
                if withdraw and recharge:
                    withdraw_line.append((day, withdraw.get('avg')))
                    recharge_line.append((day, recharge.get('avg')))
                    inflow = recharge.get('tot')
                    outflow = withdraw.get('tot')
                    in_bar.append((day, inflow))
                    out_bar.append((day, outflow))
                    net_bar.append((day, inflow - outflow))

            start, end = fill_data(in_bar)
            fill_data(out_bar)
            fill_data(withdraw_line)
            fill_data(recharge_line)
            fill_data(net_bar)

            return Response({'in_bar': {'data': in_bar, 'name': _(u'总流入')},
                             'out_bar': {'data': out_bar, 'name': _(u'总流出')},
                             'withdraw_line': {'data': withdraw_line, 'name': _(u'笔均提现')},
                             'recharge_line': {'data': recharge_line, 'name': _(u'笔均充值')},
                             'net_bar': {'data': net_bar, 'name': _(u'净流入')},
                             'start': start, 'end': end})
        return data_bad_response()
