# coding: utf-8
'''
Created on 2018年3月15日

@author: likun
'''

from django.conf.urls import url
from usercenter.views import LoginAPIView, RegisterAPIView, LoginVcodeView, LoginEcodeAPIView, \
    LoginCheckUsernameAPIView, LoginCheckEmailAPIView, LoginCheckVcodeAPIView, LoginCheckEcodeAPIView,\
    MemberServiceListAPIView, MemberOrderListAPIView, MemberPaymentAPIView,\
    SubscribeSettingAPIView, SubscribeListAPIView, MemberPaymentCallbackAPIView,\
    IosPayCheck, ChangePasswordAPIView, MemberStatusAPIView,\
    SubscribeCancelAPIView, UserInvitationAPIView,\
    UserBalanceListAPIView

urlpatterns = [
    url(r'^login/$', LoginAPIView.as_view(), name='user_login'),
    url(r'^change/password/$', ChangePasswordAPIView.as_view(),
        name='user_change_password'),
    url(r'^get_vcode/$', LoginVcodeView.as_view(), name='user_get_vcode'),
    url(r'^get_ecode/$', LoginEcodeAPIView.as_view(), name='user_get_ecode'),
    url(r'^check/username/$', LoginCheckUsernameAPIView.as_view(),
        name='user_check_usename'),
    url(r'^check/email/$', LoginCheckEmailAPIView.as_view(), name='user_check_email'),
    url(r'^check/vcode/$', LoginCheckVcodeAPIView.as_view(), name='user_check_vcode'),
    url(r'^check/ecode/$', LoginCheckEcodeAPIView.as_view(), name='user_check_ecode'),
    url(r'^check/status/$', MemberStatusAPIView.as_view(), name='user_check_status'),
    url(r'^register/$', RegisterAPIView.as_view(), name='user_register'),
    url(r'^member/$', MemberServiceListAPIView.as_view(), name='user_member_list'),
    url(r'^order/$', MemberOrderListAPIView.as_view(), name='user_order_list'),
    url(r'^payment/$', MemberPaymentAPIView.as_view(), name='user_payment'),
    url(r'^payment/callback/$',
        MemberPaymentCallbackAPIView.as_view(), name='user_payment'),
    url(r'^subscribe/setting/$', SubscribeSettingAPIView.as_view(),
        name='user_subscribe_setting'),
    url(r'^subscribe/list/$', SubscribeListAPIView.as_view(),
        name='user_subscribe_list'),
    url(r'^subscribe/cancel/$', SubscribeCancelAPIView.as_view(),
        name='user_subscribe_cancel'),
    url(r'^pay_check/$', IosPayCheck.as_view(),
        name='user_pay_check'),

    url(r'^invitation/$', UserInvitationAPIView.as_view(), name='user_invitation'),
    url(r'^balance/list/$', UserBalanceListAPIView.as_view(),
        name='user_balance_list'),
]
