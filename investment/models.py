# coding: utf-8
from django.db import models
from django.utils.translation import gettext_lazy as _
from common.modelUtils import StatusMixin, TimestampMixin
from usercenter.models import User


class PositionSubscribe(StatusMixin, TimestampMixin):
    user = models.ForeignKey(User, verbose_name=_(u'用户'))

    class Meta:
        verbose_name = verbose_name_plural = _(u'持仓订阅')


class TransactionSubscribe(StatusMixin, TimestampMixin):
    user = models.ForeignKey(User, verbose_name=_(u'用户'))
    address = models.CharField(max_length=64)

    class Meta:
        verbose_name = verbose_name_plural = _(u'交易订阅')
