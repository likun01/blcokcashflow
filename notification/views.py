# # coding: utf-8
# '''
# Created on 2018年3月27日
#
# @author: likun
# '''
# from django.db.models import Q
# from rest_framework.generics import ListAPIView
# from notification.serializers import NotificationSerializer
# from notification.v2.serializers import NotificationSerializer as NotificationSerializerV2
# from notification.models import Notification, UserRead
# from rest_framework.views import APIView
# from mobile.models import UsersUser
# import datetime
# from rest_framework.response import Response
# from common.rest_utils import login_required_response, data_bad_response,\
#     app_device, app_token, app_device_required, api_version_number
#
#
# class NotificationListAPIView(ListAPIView):
#     '''
#     消息列表
#
#     - category: 消息类别(usermessage: 系统, usersvalidate: 验证 ,userscomment: 评论, usersbravo: 点赞)
#     - token
#     - device
#     '''
#     serializer_class = NotificationSerializer
#
#     def get_serializer_class(self):
#         if api_version_number(self.request) > 1:
#             return NotificationSerializerV2
#         return NotificationSerializer
#
#     def get_queryset(self):
#         data = self.request.query_params
#         token = app_token(self.request)
#         device = app_device(self.request)
#         ct = data.get('category')
#
#         user_id = None
#         if token:
#             try:
#                 user_id = UsersUser.objects.get(active_token=token).pk
#             except UsersUser.DoesNotExist:
#                 pass
#
#         qs = Notification.objects.prefetch_related('content_object').filter(
#             ntf_type__in=['all', 'inner'], content_type__model=ct, push_status__in=('done', 'send'))
#         if ct == 'usermessage':
#             qs = qs.filter(
#                 usermessage__expired_datetime__gte=datetime.datetime.now())
#             userread = UserRead.objects.filter(device=device)
#             if user_id:
#                 qs = qs.filter(
#                     Q(receiver__isnull=True) | Q(receiver_id=user_id))
#                 userread = UserRead.objects.filter(
#                     Q(user_id=user_id) | Q(device=device))
#             else:
#                 qs = qs.filter(receiver__isnull=True)
#
#             ntf = qs.filter(receiver__isnull=True)
#             ntf_ids = map(lambda x: x.pk, ntf)
#             read_ids = map(
#                 lambda x: x.notification_id, userread.filter(notification_id__in=ntf_ids))
#             unread_ntf_ids = set(ntf_ids) ^ set(read_ids)
#             notifications = []
#             for ntf_id in unread_ntf_ids:
#                 notifications.append(
#                     UserRead(notification_id=ntf_id, user_id=user_id, device=device))
#             UserRead.objects.bulk_create(notifications)
#         else:
#             qs = qs.filter(receiver_id=user_id)
#
#         qs.filter(is_read=False, receiver__isnull=False).update(is_read=True)
#
#         return qs
#
#     @app_device_required
#     def get(self, request, *args, **kwargs):
#         data = request.query_params
#         token = app_token(request)
#         device = app_device(request)
#         ct = data.get('category')
#         if not ct or (ct == 'usermessage' and not device) or (ct != 'usermessage' and not token):
#             return data_bad_response()
#
#         if token and (not UsersUser.objects.filter(active_token=token).exists()):
#             return login_required_response()
#         return super(NotificationListAPIView, self).get(request, *args, **kwargs)
#
#
# class NotificationReveiveAPIView(APIView):
#     '''
#      接收消息
#
#     - token
#     - device
#     '''
#     @app_device_required
#     def get(self, request, *args, **kwargs):
#         device = app_device(request)
#         token = app_token(request)
#         user_id = None
#         if token:
#             try:
#                 user_id = UsersUser.objects.get(active_token=token).pk
#             except UsersUser.DoesNotExist:
#                 return login_required_response()
#
#         res = {'usermessage': {'count': 0, 'desc': ''}, 'usersvalidate': {'count': 0, 'desc': ''},
#                'userscomment': {'count': 0, 'desc': ''}, 'usersbravo': {'count': 0, 'desc': ''}}
#         qs = Notification.objects.filter(
#             ntf_type__in=['all', 'inner'], push_status__in=('done', 'send'))
#         messages = qs.filter(content_type__model='usermessage',
#                              usermessage__expired_datetime__gte=datetime.datetime.now())
#         if user_id:
#             messages = messages.filter(
#                 Q(receiver__isnull=True) | Q(receiver_id=user_id))
#             userread = UserRead.objects.filter(
#                 Q(user_id=user_id) | Q(device=device))
#             ntf_ids = map(lambda x: x.pk, messages.filter(is_read=False))
#             read_ids = map(
#                 lambda x: x.notification_id, userread.filter(notification_id__in=ntf_ids))
#             unread_ntf_ids = set(ntf_ids) ^ set(read_ids)
#             messages_first = messages.first()
#             if messages_first:
#                 res.update(
#                     {'usermessage': {'count': len(unread_ntf_ids), 'desc': messages_first.desc}})
#
#             usersvalidate = qs.filter(
#                 content_type__model='usersvalidate', receiver_id=user_id)
#             usersvalidate_first = usersvalidate.first()
#             if usersvalidate_first:
#                 res.update({'usersvalidate': {
#                            'count': usersvalidate.filter(is_read=False).count(), 'desc': usersvalidate_first.desc}})
#             userscomment = qs.filter(
#                 content_type__model='userscomment', receiver_id=user_id)
#             userscomment_first = userscomment.first()
#             if userscomment_first:
#                 res.update(
#                     {'userscomment': {'count': userscomment.filter(is_read=False).count(), 'desc': userscomment_first.desc}})
#
#             usersbravo = qs.filter(
#                 content_type__model='usersbravo', receiver_id=user_id)
#             usersbravo_first = usersbravo.first()
#             if usersbravo_first:
#                 res.update(
#                     {'usersbravo': {'count': usersbravo.filter(is_read=False).count(), 'desc': usersbravo_first.desc}})
#         else:
#             userread = UserRead.objects.filter(device=device)
#             messages = messages.filter(receiver__isnull=True)
#             ntf_ids = map(lambda x: x.pk, messages)
#             read_ids = map(
#                 lambda x: x.notification_id, userread.filter(notification_id__in=ntf_ids))
#             unread_ntf_ids = set(ntf_ids) ^ set(read_ids)
#             desc = messages.first() and messages.first().desc or ''
#             res.update(
#                 {'usermessage': {'count': len(unread_ntf_ids), 'desc': desc}})
#         count = sum(map(lambda x: x.get('count'), res.values()))
#         return Response({'code': 0, 'count': count, 'results': res})
