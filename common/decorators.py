# coding: utf-8
'''
Created on 2016年5月24日

@author: likun
'''
from functools import wraps
from common.utils import debug
import time


def debug_time(view_func):
    @wraps(view_func)
    def wrapped_view(*args, **kwargs):
        st = time.time()
        res = view_func(*args, **kwargs)
        ed = time.time()
        debug(view_func.__name__, ed - st)
        return res
    return wrapped_view
