# # coding: utf-8
# '''
# Created on 2018年3月27日
#
# @author: likun
# '''
# from notification.models import Notification, UserMessage
# from rest_framework import serializers
# from mobile.models import UsersValidate, UsersComment, UsersBravo
# from mobile.serializers import UserValidateListSerializer, UserBravoSerializer,\
#     UserMineCommentListSerializer
#
#
# class UserMessageSerializer(serializers.ModelSerializer):
#     urlscheme = serializers.CharField()
#
#     class Meta:
#         model = UserMessage
#         fields = (
#             'title', 'image', 'summary', 'message_type', 'type_link', 'type_id', 'urlscheme')
#
#
# class NotificationRelatedField(serializers.RelatedField):
#
#     def to_representation(self, value):
#         if isinstance(value, UserMessage):
#             serializer = UserMessageSerializer(value)
#         elif isinstance(value, UsersValidate):
#             serializer = UserValidateListSerializer(value)
#         elif isinstance(value, UsersComment):
#             serializer = UserMineCommentListSerializer(value)
#         elif isinstance(value, UsersBravo):
#             serializer = UserBravoSerializer(value)
#         else:
#             raise Exception('Unexpected type of tagged object')
#
#         return serializer.data
#
#
# class NotificationSerializer(serializers.ModelSerializer):
#     message = NotificationRelatedField(read_only=True, source='content_object')
#     push_datetime_timestamp = serializers.IntegerField()
#
#     class Meta:
#         model = Notification
#         fields = (
#             'message', 'desc', 'push_datetime', 'push_datetime_timestamp')
