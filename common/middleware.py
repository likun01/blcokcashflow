# coding: utf-8
'''
Created on 2018年3月21日

@author: likun
'''

import re
import urllib2
from django.http.response import HttpResponse, HttpResponseServerError,\
    HttpResponseNotFound, HttpResponseBadRequest
from django.conf import settings
from urllib2 import HTTPError


class NodeAPIRedirectMiddleware(object):
    NOT_IGNORABLE_URLS = (
        re.compile(r'^/api/balance/'),
        re.compile(r'^/api/income/'),
        re.compile(r'^/api/expend/'),
        re.compile(r'^/api/in_times/'),
        re.compile(r'^/api/exp_times/'),
        re.compile(r'^/api/account/'),
        re.compile(r'^/api/chart/'),
        re.compile(r'^/api/home/'),
        re.compile(r'^/api/currency/'),
        re.compile(r'^/api/trade/'),
        re.compile(r'^/api/user/'),
        re.compile(r'^/api/unconf'),
        re.compile(r'^/api/back/'),
    )

    def is_not_ignorable_request(self, request):
        self.path = request.get_full_path()
        return any(pattern.search(self.path) for pattern in self.NOT_IGNORABLE_URLS)

    def process_response(self, request, response):
        if self.is_not_ignorable_request(request):
            url = '{0}{1}'.format(settings.NODE_SERVER, self.path)
            req = urllib2.Request(url, headers=request.META)
            try:
                conn = urllib2.urlopen(req)
                info = conn.info()
                data = conn.read()
                return HttpResponse(data, content_type=info.get("content-type"))
            except HTTPError as e:
                if e.code == '400':
                    return HttpResponseBadRequest()
                if e.code == '404':
                    return HttpResponseNotFound()
                if e.code == '500':
                    return HttpResponseServerError()
        return response
