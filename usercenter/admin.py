# coding: utf-8
from django.contrib import admin
from usercenter.models import User, MemberService, MemberOrder,\
    MemberOrderNotificationRecord, SubscribeSetting


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_member',
                    'member_last_date', 'token')
    list_filter = ('is_member',)
    search_fields = ('username', 'email',)
    date_hierarchy = 'date_joined'


@admin.register(MemberService)
class MemberServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'coin_type', 'duration',
                    'price', 'discount', 'status')
    list_filter = ('coin_type', 'status')
    search_fields = ('name',)


@admin.register(MemberOrder)
class MemberOrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'invoice_id', 'user', 'service', 'start_date', 'end_date', 'coin_type', 'coin_amount', 'url',
                    'status', 'exception_status')
    list_filter = ('status', 'exception_status', 'coin_type')
    search_fields = ('user__username', 'user__email',
                     'order_id', 'guid', 'invoice_id',)
    date_hierarchy = 'created_datetime'


@admin.register(MemberOrderNotificationRecord)
class MemberOrderNotificationRecordAdmin(admin.ModelAdmin):
    list_display = ('order', 'invoice_id', 'user',
                    'status', 'exception_status')
    list_filter = ('status', 'exception_status',)
    search_fields = ('user__username', 'user__email',
                     'order__order_id', 'invoice_id',)
    date_hierarchy = 'created_datetime'


@admin.register(SubscribeSetting)
class SubscribeSettingAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_time', 'end_time',
                    'status')
    list_filter = ('status',)
    search_fields = ('user__username', 'user__email',)
