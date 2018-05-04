# coding: utf-8
'''
Created on 2018年3月22日

@author: likun
'''

from django.conf.urls import url
from investment.views import PositionListAPIView,\
    PositionWarningSubscribeAPIView, TransactionAPIView, QuotationListAPIView,\
    TransactionWarningSubscribeAPIView, ExchangeAPIView, ExchangeAVGAPIView,\
    ImagesTempAPIView

urlpatterns = [
    url('^quotation/$', QuotationListAPIView.as_view(), name='quotation_charts'),
    url('^position/$', PositionListAPIView.as_view(), name='position_charts'),
    url('^position/subscribe/$', PositionWarningSubscribeAPIView.as_view(),
        name='position_subscribe'),
    url('^transaction/$', TransactionAPIView.as_view(),
        name='transaction_charts'),
    url('^transaction/subscribe/$', TransactionWarningSubscribeAPIView.as_view(),
        name='transaction_subscribe'),
    url('^exchange/$', ExchangeAPIView.as_view(),
        name='exchange_charts'),
    url('^exchange/avg/$', ExchangeAVGAPIView.as_view(),
        name='exchange_charts_avg'),
    url('^send/images/$', ImagesTempAPIView.as_view(),
        name='exchange_send_images'),
]
