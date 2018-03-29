# coding: utf-8
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.modelUtils import TimestampMixin
from usercenter.models import User

POSITIONWARNING_CHANGE_CHOICES = (
    ('up', _(u'上涨')),
    ('down', _(u'下跌')),
)


class PositionWarning(TimestampMixin):
    user = models.ForeignKey(User, verbose_name=_(u'用户'))
    change = models.CharField(_(u'涨跌'), max_length=14,
                              choices=POSITIONWARNING_CHANGE_CHOICES)
    percent = models.IntegerField(_(u'百分之'), default=0)
    pushed = models.BooleanField(_(u'已推送'), default=False)

    class Meta:
        verbose_name = verbose_name_plural = _(u'持仓预警')


class TransactionWarning(TimestampMixin):
    user = models.ForeignKey(User, verbose_name=_(u'用户'))
    address = models.CharField(max_length=64, db_index=True)
    amount = models.DecimalField(max_digits=20, decimal_places=10)
    pushed = models.BooleanField(_(u'已推送'), default=False)

    class Meta:
        verbose_name = verbose_name_plural = _(u'交易预警')
