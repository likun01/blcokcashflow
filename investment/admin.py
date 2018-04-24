# coding: utf-8
from django.contrib import admin
from investment.models import PositionWarning, TransactionWarning


@admin.register(PositionWarning)
class PositionWarningAdmin(admin.ModelAdmin):
    list_display = ('user', 'change', 'percent', 'coin_type',
                    'created_datetime', 'modified_datetime',)
    list_filter = ('coin_type',)
    search_fields = ('user__username', 'user__email',)
    raw_id_fields = ('user',)


@admin.register(TransactionWarning)
class TransactionWarningAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'address_type', 'amount', 'coin_type',
                    'created_datetime', 'modified_datetime')
    list_filter = ('address_type', 'coin_type')
    search_fields = ('user__username', 'user__email',)

    raw_id_fields = ('user',)
