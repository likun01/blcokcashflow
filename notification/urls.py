# # coding: utf-8
# '''
# Created on 2018年3月27日
#
# @author: likun
# '''
#
# from django.conf.urls import url
# from notification.views import NotificationListAPIView,\
#     NotificationReveiveAPIView
#
# urlpatterns = [
#     url(r'^$', NotificationListAPIView.as_view(),  name='notification_list'),
#     url(r'^receive/$', NotificationReveiveAPIView.as_view(),
#         name='notification_list_receive'),
# ]
