# coding: utf-8
'''
Created on 2018年3月23日

@author: likun
'''
from celery import task

from common.decorators import debug_time
from usercenter.models import User
from django.utils.timezone import now


@task
@debug_time
def check_member():
    qs = User.objects.filter(member_last_date__lte=now())
    qs.update(is_member=False)
