# coding: utf-8
'''
Created on 2018年3月27日

@author: likun
'''
from django.db.models.aggregates import Count
from django.utils.translation import gettext_lazy as _
from celery import task

from notification.models import Notification
import datetime
from common.rest_utils import build_urlscheme
from common.decorators import debug_time
from common.utils import debug
from notification.push import PushSdk
from investment.models import PositionWarning, TransactionWarning
from common.models_ltc_db import IndexHis, TLiteSpecialAddress
from usercenter.models import Subscribe, SubscribeSetting
from django.utils.timezone import now
from django.db import connections
from blockchain_db.models import TBitSpecialAddress


@task
@debug_time
def ltc_position_warning_notification():
    '''
    LTC每小时执行，生成仓位预警提醒
    '''
    year = now().year
    month = now().month
    day = now().day
    ssuser = []
    for ss in SubscribeSetting.objects.filter(status=1):
        if (ss.start_time > ss.end_time and ss.start_time > now().time() and ss.end_time < now().time())\
                or (ss.start_time < ss.end_time and (ss.start_time > now().time() or ss.end_time < now().time())):
            ssuser.append(ss.user.pk)

    qs = PositionWarning.objects.filter(user__in=ssuser, coin_type='LTC',
                                        created_datetime__year=year, created_datetime__month=month, created_datetime__day=day, pushed=False)
    for obj in qs:
        desc = _(u'莱特币:仓位{}了{}%').format(
            obj.get_change_display(), obj.percent)
        Notification.objects.create(receiver=obj.user, content_object=obj,
                                    desc=desc, push_status='done', push_datetime=now())

    if qs.exists():
        users = qs.values('user').annotate(
            count=Count('user')).order_by('user')
        users_count = len(users)
        max_alias_const = 100
        max_alias = users_count if users_count < max_alias_const else max_alias_const
        sdk = PushSdk()

        for step in range(0, users_count, max_alias):
            real_alias = users_count % max_alias if users_count - \
                step < max_alias else max_alias
            push_notifications = []
            urlscheme = build_urlscheme('app')
            for index in xrange(0, real_alias):
                user = users[index + step]
                push_notifications.append(Notification(
                    receiver_id=user.get('user'), content_object=obj, desc=desc,
                    ntf_type='push', push_required=False, push_status='done', push_datetime=now(), urlscheme=urlscheme))
            aliases = users[step:step + real_alias]
            r, info = sdk.publish_to_alias_batch(
                map(lambda x: str(x.get('user')), aliases), _(u'莱特币持仓预警'), desc, urlscheme)
            Notification.objects.bulk_create(push_notifications)
            debug('ltc_position_warning_notification', (r, info))
        qs.update(pushed=True)


@task
@debug_time
def btc_position_warning_notification():
    '''
    BTC每小时执行，生成仓位预警提醒
    '''
    year = now().year
    month = now().month
    day = now().day
    ssuser = []
    for ss in SubscribeSetting.objects.filter(status=1):
        if (ss.start_time > ss.end_time and ss.start_time > now().time() and ss.end_time < now().time())\
                or (ss.start_time < ss.end_time and (ss.start_time > now().time() or ss.end_time < now().time())):
            ssuser.append(ss.user.pk)

    qs = PositionWarning.objects.filter(user__in=ssuser, coin_type='BTC',
                                        created_datetime__year=year, created_datetime__month=month, created_datetime__day=day, pushed=False)
    for obj in qs:
        desc = _(u'比特币:仓位{}了{}%').format(
            obj.get_change_display(), obj.percent)
        Notification.objects.create(receiver=obj.user, content_object=obj,
                                    desc=desc, push_status='done', push_datetime=now())

    if qs.exists():
        users = qs.values('user').annotate(
            count=Count('user')).order_by('user')
        users_count = len(users)
        max_alias_const = 100
        max_alias = users_count if users_count < max_alias_const else max_alias_const
        sdk = PushSdk()

        for step in range(0, users_count, max_alias):
            real_alias = users_count % max_alias if users_count - \
                step < max_alias else max_alias
            push_notifications = []
            urlscheme = build_urlscheme('app')
            for index in xrange(0, real_alias):
                user = users[index + step]
                push_notifications.append(Notification(
                    receiver_id=user.get('user'), content_object=obj, desc=desc,
                    ntf_type='push', push_required=False, push_status='done', push_datetime=now(), urlscheme=urlscheme))
            aliases = users[step:step + real_alias]
            r, info = sdk.publish_to_alias_batch(
                map(lambda x: str(x.get('user')), aliases), _(u'比特币持仓预警'), desc, urlscheme)
            Notification.objects.bulk_create(push_notifications)
            debug('btc_position_warning_notification', (r, info))
        qs.update(pushed=True)


@task
@debug_time
def transaction_warning_notification():
    '''
    每小时执行，生成交易地址预警提醒
    '''
    year = now().year
    month = now().month
    day = now().day
    ssuser = []
    for ss in SubscribeSetting.objects.filter(status=1):
        if (ss.start_time > ss.end_time and ss.start_time > now().time() and ss.end_time < now().time())\
                or (ss.start_time < ss.end_time and (ss.start_time > now().time() or ss.end_time < now().time())):
            ssuser.append(ss.user.pk)

    qs = TransactionWarning.objects.filter(user__in=ssuser,
                                           created_datetime__year=year, created_datetime__month=month, created_datetime__day=day, pushed=False)
    for obj in qs:
        desc = _(u'交易预警:{}有新的{}交易,交易量为{}币').format(
            obj.address_type == 1 and u'赚钱账户' or u'韭菜账户', obj.get_change_display(), obj.amount)
        Notification.objects.create(receiver=obj.user, content_object=obj,
                                    desc=desc, push_status='done', push_datetime=now())

    if qs.exists():
        users = qs.values('user').annotate(
            count=Count('user')).order_by('user')
        users_count = len(users)
        max_alias_const = 100
        max_alias = users_count if users_count < max_alias_const else max_alias_const
        sdk = PushSdk()

        for step in range(0, users_count, max_alias):
            real_alias = users_count % max_alias if users_count - \
                step < max_alias else max_alias
            push_notifications = []
            urlscheme = build_urlscheme('app')
            for index in xrange(0, real_alias):
                user = users[index + step]
                push_notifications.append(Notification(
                    receiver_id=user.get('user'), content_object=obj, desc=desc,
                    ntf_type='push', push_required=False, push_status='done', push_datetime=now(), urlscheme=urlscheme))
            aliases = users[step:step + real_alias]
            r, info = sdk.publish_to_alias_batch(
                map(lambda x: str(x.get('user')), aliases), _(u'交易预警'), u'您订阅的地址有了新的交易行情', urlscheme)
            Notification.objects.bulk_create(push_notifications)
            debug('transaction_warning_notification', (r, info))
        qs.update(pushed=True)


@task
@debug_time
def ltc_transaction_warning_notification_one_by_one():
    '''
    LTC每小时执行，生成交易地址预警提醒
    '''
    year = now().year
    month = now().month
    day = now().day
    ssuser = []
    for ss in SubscribeSetting.objects.filter(status=1):
        if (ss.start_time > ss.end_time and ss.start_time > now().time() and ss.end_time < now().time())\
                or (ss.start_time < ss.end_time and (ss.start_time > now().time() or ss.end_time < now().time())):
            ssuser.append(ss.user.pk)

    qs = TransactionWarning.objects.filter(user__in=ssuser, coin_type='LTC',
                                           created_datetime__year=year, created_datetime__month=month, created_datetime__day=day, pushed=False)

    urlscheme = build_urlscheme('app')
    for obj in qs:
        desc = _(u'莱特币:{}{}****有新的{}交易,交易量为{}币').format(
            obj.address_type == 1 and u'赚钱账户' or u'韭菜账户', obj.address[:4], obj.get_change_display(), obj.amount)
        Notification.objects.create(receiver=obj.user, content_object=obj, title=u'莱特币交易预警',
                                    desc=desc, ntf_type='all', push_required=True, push_status='wait', urlscheme=urlscheme)

    qs.update(pushed=True)


@task
@debug_time
def btc_transaction_warning_notification_one_by_one():
    '''
    BTC每小时执行，生成交易地址预警提醒
    '''
    year = now().year
    month = now().month
    day = now().day
    ssuser = []
    for ss in SubscribeSetting.objects.filter(status=1):
        if (ss.start_time > ss.end_time and ss.start_time > now().time() and ss.end_time < now().time())\
                or (ss.start_time < ss.end_time and (ss.start_time > now().time() or ss.end_time < now().time())):
            ssuser.append(ss.user.pk)

    qs = TransactionWarning.objects.filter(user__in=ssuser, coin_type='BTC',
                                           created_datetime__year=year, created_datetime__month=month, created_datetime__day=day, pushed=False)

    urlscheme = build_urlscheme('app')
    for obj in qs:
        desc = _(u'比特币:{}{}****有新的{}交易,交易量为{}币').format(
            obj.address_type == 1 and u'赚钱账户' or u'韭菜账户', obj.address[:4], obj.get_change_display(), obj.amount)
        Notification.objects.create(receiver=obj.user, content_object=obj, title=u'比特币交易预警',
                                    desc=desc, ntf_type='all', push_required=True, push_status='wait', urlscheme=urlscheme)

    qs.update(pushed=True)


@task
@debug_time
def push_notification():
    '''
     推送定时通知
    '''

    now = now()
    notifications = Notification.objects.filter(push_status='wait').filter(
        push_datetime__lte=now)
    ids = map(lambda x: x.id, notifications)
    notifications.update(push_status='send')
    if ids:
        for ntf in Notification.objects.filter(id__in=ids):
            ntf.push()


@task
@debug_time
def ltc_position_monitor():
    '''
    LTC持仓数据监控
    '''
    THRESHOLD = 0.05
    qs = IndexHis.objects.using('ltc').order_by('-his_date')[:2]
    today = qs[0].index_value
    yesterday = qs[1].index_value
    percent = (today - yesterday) / yesterday
    change = 'up' if percent > 0 else 'down'
    if abs(percent) >= THRESHOLD:
        warn = []
        users = Subscribe.objects.filter(
            category='position', coin_type='LTC', status=1)
        for user in users:
            warn.append(PositionWarning(
                user=user, change=change, coin_type='LTC', percent=percent))

        PositionWarning.objects.bulk_create(warn)


@task
@debug_time
def btc_position_monitor():
    '''
    BTC持仓数据监控
    '''
    THRESHOLD = 0.05
    qs = IndexHis.objects.using('btc').order_by('-his_date')[:2]
    today = qs[0].index_value
    yesterday = qs[1].index_value
    percent = (today - yesterday) / yesterday
    change = 'up' if percent > 0 else 'down'
    if abs(percent) >= THRESHOLD:
        warn = []
        users = Subscribe.objects.filter(
            category='position', coin_type='BTC', status=1)
        for user in users:
            warn.append(PositionWarning(
                user=user, change=change, coin_type='BTC', percent=percent))

        PositionWarning.objects.bulk_create(warn)


@task
@debug_time
def ltc_transaction_address_monitor():
    '''
    LTC交易地址监控
    '''
    MAX_AMOUNT = 5
    address_qs = Subscribe.objects.filter(
        category='transaction', coin_type='LTC', status=1).only('address')
    addresses = map(lambda x: x.address, address_qs)
    sql = '''
            SELECT
                address ,
                block_time ,
                input_value ,
                output_value
            FROM
                ltc_db.litecoin_cashflow_output
            WHERE
                address IN %s
            AND block_time > %s
            ORDER BY
                block_time DESC
            
        '''
    cursor = connections['ltc'].cursor()
    cursor.execute(
        sql, [tuple(addresses), now() - datetime.timedelta(seconds=60 * 60)])
    qs = cursor.fetchall()

    warn = []
    for address, block_time, input_value, output_value in qs:
        if abs(input_value - output_value) >= MAX_AMOUNT:

            users = Subscribe.objects.filter(
                category='transaction', address=address, coin_type='LTC', status=1).only('user')
            address_type = TLiteSpecialAddress.objects.using(
                'ltc').get(address=address).address_type
            for user in users:
                amount = input_value - output_value
                change = 'buy' if amount < 0 else 'sell'
                warn.append(TransactionWarning(
                    user=user.user, address=user.address, address_type=address_type, coin_type='LTC', amount=abs(amount), change=change, block_time=block_time))

    TransactionWarning.objects.bulk_create(warn)


@task
@debug_time
def btc_transaction_address_monitor():
    '''
    BTC交易地址监控
    '''
    MAX_AMOUNT = 5
    address_qs = Subscribe.objects.filter(
        category='transaction', coin_type='BTC', status=1).only('address')
    addresses = map(lambda x: x.address, address_qs)
    sql = '''
            SELECT
                address ,
                block_time ,
                input_value ,
                output_value
            FROM
                blockchain_db.bitcoin_cashflow_output
            WHERE
                address IN %s
            AND block_time > %s
            ORDER BY
                block_time DESC
            
        '''
    cursor = connections['btc'].cursor()
    cursor.execute(
        sql, [tuple(addresses), now() - datetime.timedelta(seconds=60 * 60)])
    qs = cursor.fetchall()

    warn = []
    for address, block_time, input_value, output_value in qs:
        if abs(input_value - output_value) >= MAX_AMOUNT:

            users = Subscribe.objects.filter(
                category='transaction', address=address, coin_type='BTC', status=1).only('user')
            address_type = TBitSpecialAddress.objects.using(
                'btc').get(address=address).address_type
            for user in users:
                amount = input_value - output_value
                change = 'buy' if amount < 0 else 'sell'
                warn.append(TransactionWarning(
                    user=user.user, address=user.address, address_type=address_type, coin_type='BTC', amount=abs(amount), change=change, block_time=block_time))

    TransactionWarning.objects.bulk_create(warn)
