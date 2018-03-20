# coding: utf-8
'''
Created on 2018年3月15日

@author: likun
'''

from django.conf.urls import url
from usercenter.views import LoginAPIView, RegisterAPIView, LoginVcodeView, LoginEcodeAPIView, \
    LoginCheckUsernameAPIView, LoginCheckEmailAPIView, LoginCheckVcodeAPIView, LoginCheckEcodeAPIView,\
    MemberServiceListAPIView, MemberOrderListAPIView, MemberPaymentAPIView,\
    SubscribeSettingAPIView, SubscribeListAPIView, MemberPaymentCallbackAPIView

urlpatterns = [
    url('^login/$', LoginAPIView.as_view(), name='user_login'),
    url('^get_vcode/$', LoginVcodeView.as_view(), name='user_get_vcode'),
    url('^get_ecode/$', LoginEcodeAPIView.as_view(), name='user_get_ecode'),
    url('^check/username/$', LoginCheckUsernameAPIView.as_view(),
        name='user_check_usename'),
    url('^check/email/$', LoginCheckEmailAPIView.as_view(), name='user_check_email'),
    url('^check/vcode/$', LoginCheckVcodeAPIView.as_view(), name='user_check_vcode'),
    url('^check/ecode/$', LoginCheckEcodeAPIView.as_view(), name='user_check_ecode'),
    url('^register/$', RegisterAPIView.as_view(), name='user_register'),
    url('^member/$', MemberServiceListAPIView.as_view(), name='user_member_list'),
    url('^order/$', MemberOrderListAPIView.as_view(), name='user_order_list'),
    url('^payment/$', MemberPaymentAPIView.as_view(), name='user_payment'),
    url('^payment/callback/$',
        MemberPaymentCallbackAPIView.as_view(), name='user_payment'),
    url('^subscribe/setting/$', SubscribeSettingAPIView.as_view(),
        name='user_subscribe_setting'),
    url('^subscribe/list/$', SubscribeListAPIView.as_view(),
        name='user_subscribe_list'),
]
