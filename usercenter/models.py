# coding: utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from common.modelUtils import StatusMixin, TimestampMixin
import jsonfield
from django.conf import settings
from common.utils import random_number, md5
from string import upper
import base64
from django.contrib.sites.models import Site
from django.db.models.aggregates import Sum


class User(AbstractUser):
    is_member = models.BooleanField(_(u'是否会员'), default=False, db_index=True)
    member_last_date = models.DateField(
        _(u'会员到期'), null=True, blank=True, db_index=True)
    token = models.CharField(_(u'token'), max_length=64, db_index=True)
    balance = models.DecimalField(
        _(u'余额'), decimal_places=9, max_digits=20, default=0.0)

    class Meta:
        verbose_name = _(u'用户')
        verbose_name_plural = _(u'用户')

    def __unicode__(self):
        return self.username

    def add_amount(self, amount):
        balance = float(self.balance)
        balance += amount
        self.balance = balance
        self.save()

    def subtract_amount(self, amount):
        balance = float(self.balance)
        if balance >= amount:
            balance -= amount
            self.balance = balance
            self.save()


class UserCode(TimestampMixin):
    user = models.OneToOneField(User, verbose_name=_(u'用户'))
    code = models.CharField(_(u'邀请码'), max_length=4,
                            db_index=True, unique=True)
    link_code = models.CharField(_(u'链接码'), max_length=8,
                                 db_index=True, unique=True)
    link = models.URLField(_(u'邀请链接'))

    class Meta:
        verbose_name = _(u'用户邀请码')
        verbose_name_plural = _(u'用户邀请码')

    def __unicode__(self):
        return self.code

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.code:
            def make_code():
                key = md5(str(random_number(8)))
                code = upper(key[:4])
                link_code = base64.b64encode(key)[:8]
                if UserCode.objects.filter(code=code).exists() or UserCode.objects.filter(link_code=link_code).exists():
                    make_code()
                return code, link_code
            code, link_code = make_code()
            link = '{}/i/{}'.format(Site.objects.get_current().domain, link_code)
            self.code = code
            self.link_code = link_code
            self.link = link

        return super(UserCode, self).save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)


class UserInvitationRecord(TimestampMixin):
    user = models.ForeignKey(User, verbose_name=_(
        u'注册用户'), related_name='inviter')
    inviter = models.ForeignKey(
        User, verbose_name=_(u'邀请用户'), related_name='invite_users', null=True, blank=True)

    class Meta:
        verbose_name = _(u'用户邀请记录')
        verbose_name_plural = _(u'用户邀请记录')

    def __unicode__(self):
        return self.user.username

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.pk is None:
            if self.inviter:
                # 邀请用户奖励
                sum_amount = UserBalanceRecord.objects.filter(
                    user=self.inviter, trans_type='invitation').aggregate(sum_amount=Sum('amount')).get('sum_amount')
                if sum_amount < settings.INVITATION_MAX_AMOUNT:
                    amount = settings.INVITATION_REGISTER_AMOUNT
                    inviter_amount = settings.INVITATION_AMOUNT
                    UserBalanceRecord.objects.create(
                        user=self.inviter, inviter=self.user, trans_type='invitation', amount=inviter_amount)
            else:
                amount = settings.REGISTER_AMOUNT
            # 注册用户奖励
            UserBalanceRecord.objects.create(
                user=self.user,  trans_type='register', amount=amount)
        return super(UserInvitationRecord, self).save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)


TRANS_TYPE_CHOICES = (
    ('invitation', u'邀请注册'),
    ('register', u'注册'),
    ('pay_member', u'购买会员'),


)


class UserBalanceRecord(TimestampMixin):
    user = models.ForeignKey(User, verbose_name=_(
        u'用户'), related_name='invite_users_banlance')
    inviter = models.ForeignKey(
        User, verbose_name=_(u'被邀请用户'), related_name='inviter_banlance', null=True, blank=True)
    trans_type = models.CharField(
        _(u'交易类型'), max_length=16, choices=TRANS_TYPE_CHOICES, db_index=True, default='invitation')
    amount = models.DecimalField(
        _(u'数量'), decimal_places=9, max_digits=20, default=0.0)

    class Meta:
        verbose_name = _(u'用户余额记录')
        verbose_name_plural = _(u'用户余额记录')
        ordering = ('-created_datetime',)

    def __unicode__(self):
        return self.user.username

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.pk is None:
            if self.trans_type in('invitation', 'register'):
                self.user.add_amount(self.amount)
            else:
                self.user.subtract_amount(self.amount)

        return super(UserBalanceRecord, self).save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)


COIN_TYPE_CHOICES = (
    ('BTC', 'BTC'),
    ('BCH', 'BCH'),
    ('ETH', 'ETH'),
    ('LTC', 'LTC'),
    ('BCF', 'BCF'),
)


class MemberService(StatusMixin, TimestampMixin):
    name = models.CharField(_(u'名称'), max_length=64)
    coin_type = models.CharField(
        _(u'币种'), max_length=32, choices=COIN_TYPE_CHOICES, db_index=True)
    duration = models.SmallIntegerField(_(u'时长'), default=0)
    price = models.DecimalField(
        _(u'金额'), decimal_places=9, max_digits=20, default=0.0)
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
SUBSCRIBE_CATEGORY_CHOICES = (
    ('position', _(u'持仓订阅')),
    ('transaction', _(u'交易订阅')),
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
        ordering = ('-created_datetime',)

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
    address = models.CharField(
        max_length=64, db_index=True, null=True, blank=True)
    coin_type = models.CharField(
        _(u'币种'), max_length=32, choices=COIN_TYPE_CHOICES, db_index=True, default='LTC')
    category = models.CharField(
        _(u'订阅类型'), db_index=True, max_length=32, choices=SUBSCRIBE_CATEGORY_CHOICES, default='position')

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
