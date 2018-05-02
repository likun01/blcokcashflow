# coding: utf-8
'''
Created on 2018年3月15日

@author: likun
'''
from rest_framework import serializers
from usercenter.models import User, MemberService, MemberOrder, SubscribeSetting,\
    Subscribe, UserBalanceRecord
from common.utils import hide_address


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'token', 'username', 'email',
                  'is_member', 'member_last_date', 'balance')


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


class UserBalanceRecordSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    is_member = serializers.SerializerMethodField()
    trans_type = serializers.CharField(source='get_trans_type_display')

    class Meta:
        model = UserBalanceRecord
        fields = ('pk', 'username', 'is_member',
                  'trans_type', 'created_datetime', 'amount')

    def get_username(self, obj):
        if obj.inviter is None:
            return obj.user.username
        return obj.inviter.username

    def get_is_member(self, obj):
        is_member = obj.user.is_member
        if obj.inviter:
            is_member = obj.inviter.is_member
        return is_member and u'VIP会员' or u'普通会员'
