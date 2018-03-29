# coding: utf-8
from django.contrib import admin
from investment.models import PositionWarning, TransactionWarning


@admin.register(PositionWarning)
class PositionWarningAdmin(admin.ModelAdmin):
    list_display = ('user', 'change', 'percent',
                    'created_datetime', 'modified_datetime',)
#     list_filter = ('status',)
    search_fields = ('user__username', 'user__email',)


@admin.register(TransactionWarning)
class TransactionWarningAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'amount',
                    'created_datetime', 'modified_datetime')
#     list_filter = ('status',)
    search_fields = ('user__username', 'user__email',)
