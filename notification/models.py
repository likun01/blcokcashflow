# coding: utf-8
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey,\
    GenericRelation


from common.modelUtils import TimestampMixin
import datetime
import uuid
from common.rest_utils import build_urlscheme
from common.utils import datetime2timestamp
from notification.push import PushSdk
from usercenter.models import User

NOTIFICATION_NTF_TYPE_CHOICES = (
    ('all', _(u'站内信+手机推送')),
    ('push', _(u'手机推送')),
    ('inner', _(u'站内信')),
)


NOTIFICATION_PUSH_STATUS_CHOICES = (
    ('wait', _(u'等待发送')),
    ('send', _(u'发送中')),
    ('done', _(u'发送完成')),
    ('fail', _(u'发送失败')),
    ('cancel', _(u'取消发送')),
)

NOTIFICATION_DEVICETYPE_CHOICES = (
    ('all', _(u'全部')),
    ('ANDROID', _(u'安卓')),
    ('iOS', _(u'苹果')),
)
APP_NOTIFICATION_TOPIC = (
    ('all', _(u'所有用户')),
    ('login', _(u'登录用户')),
    ('anonymous', _(u'未登录用户')),
    ('ios', _(u'ios测试')),
    ('aliyun_test', _(u'阿里云测试')),
    ('xinshui_test', _(u'测试')),
)

APP_CLICK_TYPE_CHOICES = (
    ('webview', _(u'内部链接')),
    ('browser', _(u'外部链接')),
    ('article', _(u'文章')),
    ('app', _(u'app首页')),
    ('message', _(u'消息列表')),
)
USERMESSAGE_STATUS_CHOICES = (
    ('0', _(u'草稿')),
    ('1', _(u'发布')),
)


class Notification(TimestampMixin):
    receiver = models.ForeignKey(
        User, verbose_name=_(u'消息接收者'), null=True, blank=True)
    content_type = models.ForeignKey(
        ContentType, verbose_name=_(u'类型'))
    object_id = models.IntegerField(_(u'object_id'))
    content_object = GenericForeignKey('content_type', 'object_id')
    title = models.CharField(_(u'标题'), max_length=512, null=True, blank=True)
    desc = models.CharField(_(u'描述'), max_length=512)
    is_read = models.BooleanField(_(u'已读'), default=False, db_index=True)
    ntf_type = models.CharField(
        _(u'消息类型'), max_length=64, choices=NOTIFICATION_NTF_TYPE_CHOICES, db_index=True, default='inner')
    devicetype = models.CharField(
        _(u'设备类型'), max_length=64, choices=NOTIFICATION_DEVICETYPE_CHOICES, db_index=True, default='all')
    push_required = models.BooleanField(
        _(u'需要推送'), default=False, db_index=True)
    push_datetime = models.DateTimeField(
        _(u'推送时间'), null=True, blank=True, db_index=True)
    push_status = models.CharField(
        _(u'推送状态'), max_length=16, default='wait', db_index=True, choices=NOTIFICATION_PUSH_STATUS_CHOICES)
    message_id = models.CharField(
        _(u'Message'), null=True, blank=True, max_length=256)
    urlscheme = models.CharField(
        _(u'urlscheme'), max_length=512, null=True, blank=True)

    class Meta:
        verbose_name = verbose_name_plural = _(u'通知')
        ordering = ('-push_datetime',)

    def __unicode__(self):
        return self.desc

    def push_datetime_timestamp(self):
        return datetime2timestamp(self.push_datetime)

    def push(self):
        if self.push_required:
            self.push_status = 'send'
            self.save(update_fields=['push_status'])
            sdk = PushSdk()
            if self.receiver:
                res, msgId = sdk.publish_to_alias(
                    self.receiver.pk.hex, self.title, self.desc, self.urlscheme)
            elif self.content_type.model == 'usermessage':
                topic = self.content_object.post_topic
                res, msgId = sdk.publish(self.devicetype,
                                         topic, self.title, self.desc, self.urlscheme)
            self.message_id = msgId
            if res:
                self.push_status = 'done'
            else:
                self.push_status = 'fail'
        else:
            self.push_status = 'done'
        self.push_datetime = datetime.datetime.now()
        self.save(update_fields=['message_id', 'push_datetime', 'push_status'])


@receiver(post_save, sender=Notification)
def push_notification(sender, instance=None, created=False, **kwargs):
    if created and instance.push_datetime == None and instance.push_status == 'wait':
        instance.push()


class UserMessage(TimestampMixin):
    id = models.UUIDField(
        primary_key=True, max_length=36, default=uuid.uuid1, editable=False)
    title = models.CharField(_(u'标题'), max_length=512)
    image = models.ImageField(_(u'头图'), upload_to='message', help_text=_(
        u'1080x388'), null=True, blank=True)
    summary = models.CharField(_(u'概要'), max_length=512)
    message_type = models.CharField(
        _(u'类型'), max_length=32, choices=APP_CLICK_TYPE_CHOICES, db_index=True, default='webview')
    type_link = models.URLField(
        _(u'链接'), max_length=512, null=True, blank=True)
    type_id = models.CharField(
        _(u'Id'), max_length=64, null=True, blank=True)
    expired_datetime = models.DateTimeField(_(u'过期时间'))
    post_datetime = models.DateTimeField(_(u'定时发布'), null=True, blank=True)
    post_users = models.ManyToManyField(
        User, verbose_name=_(u'发送给用户'), blank=True, max_length=512)
    post_topic = models.CharField(
        _(u'发送给频道'), null=True, blank=True, db_index=True, choices=APP_NOTIFICATION_TOPIC, max_length=64, default='all')
    post_method = models.CharField(
        _(u'发送途径'), max_length=64, choices=NOTIFICATION_NTF_TYPE_CHOICES, db_index=True, default='all')
    devicetype = models.CharField(
        _(u'设备类型'), max_length=64, choices=NOTIFICATION_DEVICETYPE_CHOICES, db_index=True, default='all')

    status = models.CharField(
        _(u'状态'), choices=USERMESSAGE_STATUS_CHOICES, max_length=16, db_index=True, default='0')
    post_count = models.IntegerField(_(u'发送人数'), default=0)

    ntf = GenericRelation(
        Notification, related_query_name='usermessage')

    class Meta:
        verbose_name = verbose_name_plural = _(u'平台消息')
        ordering = ('-modified_datetime', '-post_datetime', )

    def __unicode__(self):
        return self.title

    def urlscheme(self):
        return build_urlscheme(self.message_type, self.type_id, self.type_link)

    def urlscheme_quote(self):
        return build_urlscheme(self.message_type, self.type_id, self.type_link, True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.summary = self.summary.strip()
        if self.post_method in ['all', 'push']:
            if self.post_topic == 'all':
                self.post_count = 0
        super(UserMessage, self).save(force_insert=force_insert,
                                      force_update=force_update, using=using, update_fields=update_fields)


@receiver(post_save, sender=UserMessage)
def message_notification(sender, instance=None, created=False, **kwargs):
    content_type = ContentType.objects.get_for_model(instance._meta.model)
    if instance.status == '1':
        push_required = False
        if instance.post_method in ['all', 'push']:
            push_required = True
        if instance.post_topic:
            Notification.objects.update_or_create(content_type=content_type, object_id=instance.pk, defaults={'title': instance.title, 'desc': instance.summary, 'devicetype': instance.devicetype, 'platform': instance.platform,
                                                                                                              'ntf_type': instance.post_method, 'push_datetime': instance.post_datetime, 'push_required': push_required, 'urlscheme': instance.urlscheme_quote()})
    else:
        Notification.objects.filter(content_type=content_type,
                                    object_id=instance.pk).update(push_status='cancel')


@receiver(m2m_changed, sender=UserMessage.post_users.through)
def users_notification(sender, instance=None, created=False, action=None, **kwargs):
    if action == 'post_add' and instance.status == '1':
        push_required = False
        if instance.post_method in ['all', 'push']:
            push_required = True
        for user in instance.post_users.all():
            Notification.objects.create(receiver=user, content_object=instance, title=instance.title, desc=instance.summary,
                                        ntf_type=instance.post_method, push_datetime=instance.post_datetime, push_required=push_required, urlscheme=instance.urlscheme_quote())


class UserRead(TimestampMixin):
    notification = models.ForeignKey(Notification)
    user = models.ForeignKey(User, null=True)
    device = models.CharField(max_length=128, null=True, db_index=True)
