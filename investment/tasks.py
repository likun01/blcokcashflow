# coding: utf-8
'''
Created on 2018年3月23日

@author: likun
'''


from common.decorators import debug_time
from common.models_ltc_db import LiteStockCashflow
import datetime
from random import randint


@debug_time
def build_data():
    start = datetime.date(2013, 4, 28)
    end = datetime.date(2018, 3, 14)
    data = []
    days = 0
    for _ in range((end - start).days):
        days += 1
        print days
        data.append(LiteStockCashflow(address_type=1, his_date=start + datetime.timedelta(
            days=days), in_amount=randint(1000, 10000), out_amount=randint(1000, 10000)))
        data.append(LiteStockCashflow(address_type=2, his_date=start + datetime.timedelta(
            days=days), in_amount=randint(300, 1000), out_amount=randint(300, 1000)))
        data.append(LiteStockCashflow(address_type=3, his_date=start + datetime.timedelta(
            days=days), in_amount=randint(0, 300), out_amount=randint(0, 300)))
    LiteStockCashflow.objects.using('ltc').bulk_create(data)
