# coding: utf-8
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now

from common.rest_utils import app_user, app_data_required,\
    data_bad_response, app_member_required

import datetime
from rest_framework.views import APIView
from investment.models import PositionSubscribe, TransactionSubscribe
from common.utils import datetime2microsecond, avg
from common.models_blockchain import LitecoinChartsDatas
from common.models_ltc_db import IndexHis, TLiteSpecialAddress, LitecoinCashflowOutputWinneranalyst, LitecoinCashflowOutputWinneranalystBuyandsell,\
    LiteStockCashflow


class QuotationListAPIView(APIView):
    '''
    行情指数
    '''

    def get(self, request, *args, **kwargs):
        user = app_user(request)
        hq = LitecoinChartsDatas.objects.using('bc').order_by('hisdate')
        if not (user and user.is_member):
            hq = hq.filter(hisdate__lt=now() - datetime.timedelta(days=7))
        data = map(lambda x: (datetime2microsecond(x.hisdate), x.price
                              ), hq)
        return Response({'data': data})


class PositionListAPIView(APIView):
    '''
    持仓指数
    '''

    def get(self, request, *args, **kwargs):
        user = app_user(request)
        qs = IndexHis.objects.using('ltc').order_by('his_date')
        if not (user and user.is_member):
            qs = qs.filter(his_date__lt=now() - datetime.timedelta(days=7))
        data = map(lambda x: (datetime2microsecond(x.his_date), x.index_value
                              ), qs)
        return Response({'data': data})


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
        PositionSubscribe.objects.update_or_create(
            user=user, defaults={'status': status})
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
        qs = TLiteSpecialAddress.objects.using(
            'ltc').filter(address_type=address_type).only('address')
        addresses = map(lambda x: x.address, qs)
        sell_qs = LitecoinCashflowOutputWinneranalystBuyandsell.objects.using(
            'ltc').filter(address__in=addresses).only('address', 'output_value', 'input_value', 'block_time', 'trans_volume_doller').order_by('-block_time')
        buy_qs = LitecoinCashflowOutputWinneranalyst.objects.using(
            'ltc').filter(address__in=addresses).only('address', 'output_value', 'input_value', 'block_time', 'trans_volume_doller').order_by('-block_time')
        if not (user and user.is_member):
            sell_qs = sell_qs.filter(
                block_time__lt=now() - datetime.timedelta(days=7))
            buy_qs = buy_qs.filter(
                block_time__lt=now() - datetime.timedelta(days=7))
        buy_data = {}
        for buy in buy_qs:
            _arr = buy_data.get(buy.address, [])
            _arr.append(buy)
            buy_data.update({buy.address: _arr})

        buy_sell = {}
        for sell in sell_qs:
            _arr = buy_data.get(sell.address, [])
            trans = abs(sell.output_value - sell.input_value)
            b = None
            for x in _arr:
                if x.block_time < sell.block_time and abs(
                        x.output_value - x.input_value) > trans:
                    b = x
                    break
            if b:
                points = buy_sell.get('{}{}'.format(
                    b.address, b.block_time), {})
                sell_arr = points.get('sell', [])
                buy_price = float(b.trans_volume_doller /
                                  (b.output_value - b.input_value))
                sell_price = float(sell.trans_volume_doller /
                                   (sell.output_value - sell.input_value))
                profit = '{:.2%}'.format((sell_price - buy_price) / buy_price)
                address = '{0}{1}'.format(
                    b.address[:4], (len(b.address) - 4) * '*')
                sell_arr.append({'id': 'sell_{}'.format(sell.id), 'address': address, 'block_time': datetime2microsecond(sell.block_time), 'buy_price': buy_price,
                                 'sell_price': sell_price, 'profit': profit})
                points.update({'sell': sell_arr})

                buy = points.get('buy', {})
                sell_price_avg = avg(
                    map(lambda x: x.get('sell_price'), sell_arr))
                profit_avg = '{:.2%}'.format(
                    (sell_price_avg - buy_price) / buy_price)
                buy.update({'id': 'buy_{}'.format(b.id), 'address': address, 'block_time': datetime2microsecond(b.block_time), 'buy_price': buy_price,
                            'sell_price': sell_price_avg, 'profit': profit_avg})
                points.update({'buy': buy})

                buy_sell.update(
                    {'{}{}'.format(b.address, b.block_time): points})

        return Response({'data': buy_sell.values()})


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
        if '_' not in data.get('pk'):
            return data_bad_response()
        prefix, pk = data.get('pk').split('_')
        m = LitecoinCashflowOutputWinneranalystBuyandsell
        if prefix == 'buy':
            m = LitecoinCashflowOutputWinneranalyst
        try:
            address = m.objects.using('ltc').get(pk=pk).address
            TransactionSubscribe.objects.update_or_create(
                user=user, address=address, defaults={'status': status})
            return Response({'code': 0, 'detail': _(u'订阅成功') if status == '1' else _(u'取消成功')})
        except m.DoesNotExist:
            return data_bad_response()


class ExchangeAPIView(APIView):
    '''
    交易所行情
    '''

    def get(self, request, *args, **kwargs):
        user = app_user(request)
        qs = LiteStockCashflow.objects.using('ltc').all()
        hq = LitecoinChartsDatas.objects.using('bc').order_by('hisdate')
        if not (user and user.is_member):
            qs = qs.filter(his_date__lt=now() - datetime.timedelta(days=7))
            hq = hq.filter(hisdate__lt=now() - datetime.timedelta(days=7))

        data = {}
        map(lambda x: data.update(
            {datetime2microsecond(x.hisdate): x.price}), hq)

        def in_amount(x):
            ts = datetime2microsecond(x.his_date)
            price = data.get(ts) * float(x.in_amount) if data.get(ts) else '-'
            return (ts,  x.in_amount, price)

        def out_amount(x):
            ts = datetime2microsecond(x.his_date)
            price = data.get(ts) * float(x.out_amount) if data.get(ts) else '-'
            return (ts,  x.out_amount, price)

        l_in = map(lambda x: in_amount(x), filter(
            lambda x: x.address_type == 1, qs))
        l_out = map(lambda x: out_amount(x), filter(
            lambda x: x.address_type == 1, qs))
        m_in = map(lambda x: in_amount(x), filter(
            lambda x: x.address_type == 2, qs))
        m_out = map(lambda x: out_amount(x), filter(
            lambda x: x.address_type == 2, qs))
        s_in = map(lambda x: in_amount(x), filter(
            lambda x: x.address_type == 3, qs))
        s_out = map(lambda x: out_amount(x), filter(
            lambda x: x.address_type == 3, qs))

        def line_data(x):
            ts = x[0][0]
            amount = float(sum([x[0][1], x[1][1], x[2][1]]))
            price = data.get(ts) * amount if data.get(ts) else '-'
            return (ts, amount, price)

        in_line = map(lambda x: line_data(x), zip(l_in, m_in, s_in))
        out_line = map(lambda x: line_data(x), zip(l_out, m_out, s_out))

        def bar_data(x):
            ts = datetime2microsecond(x.his_date)
            amount = float(x.in_amount - x.out_amount)
            price = data.get(ts) * amount if data.get(ts) else '-'
            return (ts, amount, price)

        l_bar = map(lambda x: bar_data(x), filter(
            lambda x: x.address_type == 1, qs))
        s_bar = map(lambda x: bar_data(x), filter(
            lambda x: x.address_type == 2, qs))
        m_bar = map(lambda x: bar_data(x), filter(
            lambda x: x.address_type == 3, qs))

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
                         'm_bar': {'data': m_bar, 'name': _(u'中户净流入')}})
