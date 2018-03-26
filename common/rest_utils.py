# coding: utf-8
'''
Created on 2016年11月16日

@author: likun
'''
import hashlib
import time
import urllib
from functools import wraps

from django.conf import settings
from django.utils.encoding import force_bytes, iri_to_uri
from django.core.cache import cache
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from common.utils import md5
from usercenter.models import User


REST_RES_ERROR = {'code': 40004, 'detail': u'数据错误'}


class AppPermission(permissions.BasePermission):
    """
    全局权限，限制api访问
    """
#     X-APP-TIMESTAMP
#     X-APP-SIGN

    def has_permission(self, request, view):
        if request.user and hasattr(request.user, 'authenticate'):
            return True
        if getattr(view, 'api_exempt', False):
            return True
        path = request.path
        if path.startswith('/api/research/'):
            return True
        v_id = request.GET.get('v_id', '')
        if path == '/api/articles/' and v_id:
            return True
        timestamp = int(request.META.get('HTTP_X_APP_TIMESTAMP', 0))
        sign = request.META.get('HTTP_X_APP_SIGN', '').lower()
        current_timestamp = int(time.time())
        current_sign = md5('{0}{1}'.format(timestamp, settings.SECRET_KEY))

        if current_timestamp - timestamp > 30:
            return False

        if sign != current_sign:
            return False
        return True


def login_required_response():
    return Response({'code': 40003, 'detail': u'需要登录'}, status=status.HTTP_401_UNAUTHORIZED)


def member_required_response():
    return Response({'code': 40003, 'detail': u'需要购买会员'}, status=status.HTTP_401_UNAUTHORIZED)


def data_bad_response():
    return Response(REST_RES_ERROR, status=status.HTTP_400_BAD_REQUEST)


def request_data(request):
    if request.method == 'POST':
        data = request.data
    else:
        data = request.query_params.copy()
    return data


def value_from_request(request, key, header_key=''):
    value = request.META.get(header_key, '')
    if not value:
        data = request_data(request)
        value = data.get(key, '')
    return value


def app_token(request):
    return value_from_request(request, 'token', 'HTTP_X_APP_TOKEN')


def app_user(request):
    token = app_token(request)
    if token:
        try:
            user = User.objects.get(token=token)
            return user
        except User.DoesNotExist:
            pass
    return None


def app_device(request):
    return value_from_request(request, 'device', 'HTTP_X_APP_DEVICEID')


def app_verison(request):
    return value_from_request(request, 'version', 'HTTP_X_APP_VERISON')


def api_version_number(request):
    if request.version:
        return int(request.version.strip('v'))
    return 0


def app_user_agent(request):
    return request.META.get('HTTP_USER_AGENT', '')


def app_ip(request):
    ip = request.META.get(
        'HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', ''))
    return ip


def app_login_required(func):
    '''
    X-APP-TOKEN
    X-APP-DEVICEID
    '''

    @wraps(func)
    def wrapper(view, request, *wargs, **wkwargs):
        token = app_token(request)
        if token:
            try:
                user = User.objects.get(token=token)
                request.app_user = user
                return func(view, request, * wargs, **wkwargs)
            except User.DoesNotExist:
                pass
        return login_required_response()

    return wrapper


def app_member_required(func):
    '''
    X-APP-TOKEN
    X-APP-DEVICEID
    '''

    @wraps(func)
    def wrapper(view, request, *wargs, **wkwargs):
        token = app_token(request)
        if token:
            try:
                user = User.objects.get(token=token)
                if not user.is_member:
                    return member_required_response()
                request.app_user = user
                return func(view, request, * wargs, **wkwargs)
            except User.DoesNotExist:
                pass
        return login_required_response()

    return wrapper


def app_device_required(func):
    @wraps(func)
    def wrapper(view, request, *args, **kwargs):
        device = app_device(request)
        if not device:
            return data_bad_response()
        return func(view, request, * args, **kwargs)
    return wrapper


def app_user_cache(func):
    @wraps(func)
    def wrapper(view, request, *args, **kwargs):
        token = app_token(request)
        url = hashlib.md5(
            force_bytes(iri_to_uri(request.build_absolute_uri())))
        key = '{0}_{1}'.format(url.hexdigest(), token)
        data = cache.get(key)
        if not data:
            data = func(view, request, *args, **kwargs).data
            cache.set(key, data, settings.SITE_REDIS_TIMEOUT)
        return Response(data)
    return wrapper


def app_data_required(*args):
    def data_required(func):
        @wraps(func)
        def wrapper(view, request, *wrapper_args, **wrapper_kwargs):
            for key in args:
                header_keys = {'device': 'HTTP_X_APP_DEVICEID'}
                header_key = ''
                if key in header_keys.keys():
                    header_key = header_keys.get(key)
                value = value_from_request(request, key, header_key)
                if not value:
                    res = REST_RES_ERROR
                    res.update(
                        {'detail': u'{0}不能为空'.format(key)})
                    return Response(res, status=status.HTTP_400_BAD_REQUEST)
            return func(view, request, *wrapper_args, **wrapper_kwargs)
        return wrapper
    return data_required


class UnquotePageNumberPagination(PageNumberPagination):

    def get_next_link(self):
        url = super(UnquotePageNumberPagination, self).get_next_link()
        if url:
            return urllib.unquote(url)

    def get_previous_link(self):
        url = super(UnquotePageNumberPagination, self).get_previous_link()
        if url:
            return urllib.unquote(url)


class SmallPageNumberPagination(PageNumberPagination):
    page_size = 50
