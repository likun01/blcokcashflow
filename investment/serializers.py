# coding: utf-8
'''
Created on 2018年3月22日

@author: likun
'''
from rest_framework import serializers
from common.models_blockchain import LitecoinChartsDatas
from common.models_ltc_db import IndexHis


class IndexHisSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndexHis
        fields = ('index_value', 'his_date')


class LitecoinChartsDatasSerializer(serializers.ModelSerializer):
    class Meta:
        model = LitecoinChartsDatas
        fields = ('price', 'hisdate')
