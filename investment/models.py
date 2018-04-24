# coding: utf-8
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.modelUtils import TimestampMixin
from usercenter.models import User, COIN_TYPE_CHOICES

POSITIONWARNING_CHANGE_CHOICES = (
    ('up', _(u'上涨')),
    ('down', _(u'下跌')),
)

TRANSACTIONWARNING_CHANGE_CHOICES = (
    ('buy', _(u'买入')),
    ('sell', _(u'卖出')),
)
TRANSACTIONWARNING_ADDRESS_TYPE_CHOICES = (
    (1, _(u'赚钱账户')),
    (2, _(u'韭菜账户')),
)


class PositionWarning(TimestampMixin):
    user = models.ForeignKey(User, verbose_name=_(u'用户'))
    change = models.CharField(_(u'涨跌'), max_length=14,
                              choices=POSITIONWARNING_CHANGE_CHOICES)
    percent = models.IntegerField(_(u'百分之'), default=0)
    coin_type = models.CharField(
        _(u'币种'), max_length=32, choices=COIN_TYPE_CHOICES, db_index=True, default='LTC')
    pushed = models.BooleanField(_(u'已推送'), default=False, db_index=True)

    class Meta:
        verbose_name = verbose_name_plural = _(u'持仓预警')


class TransactionWarning(TimestampMixin):
    user = models.ForeignKey(User, verbose_name=_(u'用户'))
    address = models.CharField(max_length=64, db_index=True)
    address_type = models.IntegerField(
        _(u'地址类型'), choices=TRANSACTIONWARNING_ADDRESS_TYPE_CHOICES, default=1)
    change = models.CharField(_(u'涨跌'), max_length=14,
                              choices=TRANSACTIONWARNING_CHANGE_CHOICES, default='buy')
    amount = models.DecimalField(max_digits=20, decimal_places=10)
    block_time = models.DateTimeField(_(u'交易时间'), null=True, blank=True)
    coin_type = models.CharField(
        _(u'币种'), max_length=32, choices=COIN_TYPE_CHOICES, db_index=True, default='LTC')
    pushed = models.BooleanField(_(u'已推送'), default=False, db_index=True)

    class Meta:
        verbose_name = verbose_name_plural = _(u'交易预警')
