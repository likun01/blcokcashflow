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
from common.models_ltc_db import IndexHis
from usercenter.models import Subscribe


@task
@debug_time
def position_warning_notification():
    '''
    每天早上8点执行，生成预警提醒
    '''
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day

    qs = PositionWarning.objects.filter(
        created_datetime__year=year, created_datetime__month=month, created_datetime__day=day, pushed=False)
    for obj in qs:
        desc = _(u'持仓预警：仓位{}了{}%'.format(
            obj.get_change_display(), obj.percent))
        Notification.objects.create(receiver=obj.user, content_object=obj,
                                    desc=desc, push_status='done', push_datetime=datetime.datetime.now())

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
                    ntf_type='push', push_required=True, push_status='done', push_datetime=datetime.datetime.now(), urlscheme=urlscheme))
            aliases = users[step:step + real_alias]
            _, info = sdk.publish_to_alias_batch(
                map(lambda x: str(x.get('user')), aliases), _(u'持仓预警'), desc, urlscheme)
            Notification.objects.bulk_create(push_notifications)
            debug('position_warning_notification', info)
        qs.update(pushed=True)


@task
@debug_time
def transaction_warning_notification():
    '''
    每天早上8点执行，生成预警提醒
    '''
    year = datetime.datetime.now().year
    month = datetime.datetime.now().month
    day = datetime.datetime.now().day
    qs = TransactionWarning.objects.filter(
        created_datetime__year=year, created_datetime__month=month, created_datetime__day=day, pushed=False)
    for obj in qs:
        desc = _(u'交易预警：订阅地址{}有了新的交易,交易量{}'.format(
            obj.address, obj.amount))
        Notification.objects.create(receiver=obj.user, content_object=obj,
                                    desc=desc, push_status='done', push_datetime=datetime.datetime.now())

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
                    ntf_type='push', push_required=True, push_status='done', push_datetime=datetime.datetime.now(), urlscheme=urlscheme))
            aliases = users[step:step + real_alias]
            _, info = sdk.publish_to_alias_batch(
                map(lambda x: str(x.get('user')), aliases), _(u'交易预警'), desc, urlscheme)
            Notification.objects.bulk_create(push_notifications)
            debug('transaction_warning_notification', info)
        qs.update(pushed=True)


@task
@debug_time
def push_notification():
    '''
     推送定时通知
    '''

    now = datetime.datetime.now()
    notifications = Notification.objects.filter(push_status='wait').filter(
        push_datetime__lte=now)
    ids = map(lambda x: x.id, notifications)
    notifications.update(push_status='send')
    if ids:
        for ntf in Notification.objects.filter(id__in=ids):
            ntf.push()


@task
@debug_time
def position_monitor():
    '''
    持仓数据监控
    '''
    THRESHOLD = 0.05
    qs = IndexHis.objects.using('ltc').order_by('-his_date')[:2]
    today = qs[0].index_value
    yesterday = qs[1].index_value
    percent = (today - yesterday) / yesterday
    change = 'up' if percent > 0 else 'down'
    if abs(percent) >= THRESHOLD:
        warn = []
        users = Subscribe.objects.filter(category='position', status=1)
        for user in users:
            warn.append(PositionWarning(
                user=user, change=change, percent=percent))

        PositionWarning.objects.bulk_create(warn)
