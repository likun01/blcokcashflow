# coding: utf-8
'''
Created on 2018年3月15日

@author: likun
'''
import urllib2
import json


def get_usd_rate():
    '''
    比特币对美元汇率
    '''
    url = 'https://bitpay.com/api/rates/BTC/USD'
    response = urllib2.urlopen(url)
    data = json.loads(response.read())
    rate = float(data.get('rate'))
    return rate
