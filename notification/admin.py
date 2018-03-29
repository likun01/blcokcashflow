# coding: utf-8
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from notification.models import UserMessage, Notification
from notification.forms import UserMessageForm


@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    form = UserMessageForm
    fields = ('title', 'image', 'summary', 'message_type',
              'type_link', 'type_id', 'expired_datetime', 'post_users', 'post_topic', 'post_method', 'devicetype', 'platform', 'post_datetime', 'status')
    list_display = (
        'title', 'expired_datetime', 'status', 'post_obj', 'message_type', 'post_datetime', 'post_count')
    list_filter = ('message_type', 'post_method', 'post_topic',
                   'status', 'devicetype',)
    search_fields = ('title',)
    date_hierarchy = 'post_datetime'
    raw_id_fields = ('post_users',)

    def post_obj(self, obj):
        if obj.post_topic:
            return obj.get_post_topic_display()
        return ','.join([user.nickname() for user in obj.post_users.select_related('usersprofile').all()])

    def image_preview(self, obj):
        if obj.image:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="350"/></a>'\
                .format(obj.image.url)
        return ''

    image_preview.allow_tags = True
    image_preview.short_description = _(u'图片')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        'desc', 'ntf_type', 'receiver', 'push_datetime', 'push_status', 'message_id')
    list_filter = ('ntf_type', 'push_status')
    date_hierarchy = 'push_datetime'
    raw_id_fields = ('receiver',)
    search_fields = ('desc', 'receiver__mobile')
