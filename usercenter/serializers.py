# coding: utf-8
'''
Created on 2018年3月15日

@author: likun
'''
from rest_framework import serializers
from usercenter.models import User, MemberService, MemberOrder, SubscribeSetting,\
    Subscribe
from common.utils import hide_address


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'token', 'username', 'email',
                  'is_member', 'member_last_date')


class MemberServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = MemberService
        fields = ('id', 'name', 'coin_type', 'duration', 'price', 'discount')


class MemberOrderSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    class Meta:
        model = MemberOrder
        fields = ('order_id', 'name', 'start_date', 'end_date',
                  'created_datetime', 'coin_type', 'coin_amount', 'status', 'url', 'invoice_id')

    def get_name(self, obj):
        return obj.service.name


class SubscribeSettingSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscribeSetting
        fields = ('id', 'status', 'start_time', 'end_time')


class SubscribeSerializer(serializers.ModelSerializer):
    address = serializers.SerializerMethodField()

    class Meta:
        model = Subscribe
        fields = ('pk', 'category', 'address', 'created_datetime')

    def get_address(self, obj):
        return hide_address(obj.address)
