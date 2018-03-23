# coding: utf-8
from django.contrib import admin
from investment.models import PositionSubscribe, TransactionSubscribe


@admin.register(PositionSubscribe)
class PositionSubscribeAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_datetime', 'modified_datetime',
                    'status')
    list_filter = ('status',)
    search_fields = ('user__username', 'user__email',)


@admin.register(TransactionSubscribe)
class TransactionSubscribeAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'created_datetime', 'modified_datetime',
                    'status')
    list_filter = ('status',)
    search_fields = ('user__username', 'user__email',)
