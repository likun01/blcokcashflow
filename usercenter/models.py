# coding: utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from common.modelUtils import StatusMixin, TimestampMixin
import jsonfield


class User(AbstractUser):
    is_member = models.BooleanField(_(u'是否会员'), default=False, db_index=True)
    member_last_date = models.DateField(
        _(u'会员到期'), null=True, blank=True, db_index=True)
    token = models.CharField(_(u'token'), max_length=64, db_index=True)

    class Meta:
        verbose_name = _(u'用户')
        verbose_name_plural = _(u'用户')

    def __unicode__(self):
        return self.username


COIN_TYPE_CHOICES = (
    ('BTC', 'BTC'),
    ('BCH', 'BCH'),
    ('ETH', 'ETH'),
    ('LTC', 'LTC'),
)


class MemberService(StatusMixin, TimestampMixin):
    name = models.CharField(_(u'名称'), max_length=64)
    coin_type = models.CharField(
        _(u'币种'), max_length=32, choices=COIN_TYPE_CHOICES, db_index=True)
    duration = models.SmallIntegerField(_(u'时长'), default=0)
    price = models.DecimalField(
        _(u'金额'), decimal_places=2, max_digits=8, default=0.0)
    discount = models.SmallIntegerField(_(u'折扣'), default=10)

    class Meta:
        verbose_name = _(u'会员服务')
        verbose_name_plural = _(u'会员服务')

    def __unicode__(self):
        return self.name


ORDER_STATUS_CHOICES = (
    ('new', 'new'),
    ('paid', 'paid'),
    ('confirmed', 'confirmed'),
    ('complete', 'complete'),
    ('expired', 'expired'),
    ('invalid', 'invalid'),
)

ORDER_EXCEPTION_STATUS_CHOICES = (
    ('false', 'false'),
    ('paidPartial', 'paidPartial'),
    ('paidOver', 'paidOver'),
    ('paidLate', 'paidLate'),
)


class MemberOrder(TimestampMixin):
    user = models.ForeignKey(User, verbose_name=_(u'用户'))
    service = models.ForeignKey(MemberService, verbose_name=_(u'购买服务'))
    order_id = models.CharField(_(u'订单号'), max_length=64, db_index=True)
    guid = models.CharField(_(u'guid'), max_length=128, db_index=True)
    url = models.URLField(_(u'URL'))
    start_date = models.DateField(_(u'开始时间'))
    end_date = models.DateField(_(u'截止时间'))
    coin_type = models.CharField(
        _(u'币种'), max_length=32, choices=COIN_TYPE_CHOICES, db_index=True)
    coin_amount = models.DecimalField(
        _(u'虚拟币数量'), decimal_places=9, max_digits=20, default=0.0)
    status = models.CharField(
        _(u'状态'), max_length=32, choices=ORDER_STATUS_CHOICES, db_index=True)
    exception_status = models.CharField(
        _(u'异常状态'), max_length=32, choices=ORDER_EXCEPTION_STATUS_CHOICES)
    invoice_id = models.CharField(
        _(u'交易id'), max_length=64, db_index=True)
    addresses = jsonfield.JSONField(_(u'交易地址'))
    origin = jsonfield.JSONField(_(u'原始信息'))

    class Meta:
        verbose_name = _(u'购买订单')
        verbose_name_plural = _(u'购买订单')

    def __unicode__(self):
        return self.order_id


class MemberOrderNotificationRecord(TimestampMixin):
    order = models.ForeignKey(MemberOrder, verbose_name=_(u'购买订单'))
    user = models.ForeignKey(User, verbose_name=_(u'用户'))
    invoice_id = models.CharField(
        _(u'交易id'), max_length=64, db_index=True)
    origin = jsonfield.JSONField(_(u'原始信息'))
    status = models.CharField(
        _(u'状态'), max_length=32, choices=ORDER_STATUS_CHOICES, db_index=True)
    exception_status = models.CharField(
        _(u'异常状态'), max_length=32, choices=ORDER_EXCEPTION_STATUS_CHOICES)

    class Meta:
        verbose_name = _(u'订单通知记录')
        verbose_name_plural = _(u'订单通知记录')

    def __unicode__(self):
        return self.order.order_id


class Subscribe(StatusMixin, TimestampMixin):
    user = models.ForeignKey(User, verbose_name=_(u'用户'))

    class Meta:
        verbose_name = _(u'订阅列表')
        verbose_name_plural = _(u'订阅列表')


class SubscribeSetting(StatusMixin, TimestampMixin):
    user = models.OneToOneField(User, verbose_name=_(u'用户'))
    start_time = models.TimeField(
        _(u'开始时间'), default='00:00')
    end_time = models.TimeField(
        _(u'截止时间'), default='23:59')

    class Meta:
        verbose_name = _(u'订阅设置')
        verbose_name_plural = _(u'订阅设置')


class DeivceVcode(models.Model):
    device = models.CharField(
        _(u'device'), max_length=64, db_index=True)
    vcode = models.CharField(
        _(u'vcode'), max_length=64)


class EmailEcode(models.Model):
    email = models.EmailField(
        _(u'email'), db_index=True)
    ecode = models.CharField(
        _(u'ecode'), max_length=64)
