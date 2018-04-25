# coding: utf-8
from django.contrib import admin
from usercenter.models import User, MemberService, MemberOrder,\
    MemberOrderNotificationRecord, SubscribeSetting, Subscribe, UserCode,\
    UserInvitationRecord, UserBalanceRecord


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
    list_display = ('order_id', 'invoice_id', 'user', 'service', 'created_datetime', 'start_date', 'end_date', 'coin_type', 'coin_amount', 'url',
                    'status', 'exception_status', 'modified_datetime')
    list_filter = ('status', 'exception_status', 'coin_type')
    search_fields = ('user__username', 'user__email',
                     'order_id', 'guid', 'invoice_id',)
    date_hierarchy = 'created_datetime'
    raw_id_fields = ('user',)


@admin.register(MemberOrderNotificationRecord)
class MemberOrderNotificationRecordAdmin(admin.ModelAdmin):
    list_display = ('order', 'invoice_id', 'user',
                    'status', 'exception_status')
    list_filter = ('status', 'exception_status',)
    search_fields = ('user__username', 'user__email',
                     'order__order_id', 'invoice_id',)
    date_hierarchy = 'created_datetime'
    raw_id_fields = ('user', 'order')


@admin.register(SubscribeSetting)
class SubscribeSettingAdmin(admin.ModelAdmin):
    list_display = ('user', 'start_time', 'end_time',
                    'status')
    list_filter = ('status',)
    search_fields = ('user__username', 'user__email',)
    raw_id_fields = ('user',)


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'coin_type', 'address', 'created_datetime', 'modified_datetime',
                    'status')
    list_filter = ('status', 'category', 'coin_type',)
    search_fields = ('user__username', 'user__email',)
    raw_id_fields = ('user',)


@admin.register(UserCode)
class UserCodeAdmin(admin.ModelAdmin):
    list_display = ('user', 'code', 'link_code', 'link')

    search_fields = ('code', 'user__username', 'user__email',)
    raw_id_fields = ('user',)


@admin.register(UserInvitationRecord)
class UserInvitationRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'inviter', 'created_datetime',)

    search_fields = ('inviter__username', 'inviter__email',
                     'user__username', 'user__email',)
    raw_id_fields = ('user', 'inviter')


@admin.register(UserBalanceRecord)
class UserBalanceRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'inviter', 'trans_type',
                    'amount', 'created_datetime',)
    list_filter = ('trans_type',)
    search_fields = ('inviter__username', 'inviter__email',
                     'user__username', 'user__email',)
    raw_id_fields = ('user', 'inviter')
