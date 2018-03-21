# coding: utf-8
'''
Created on 2018年3月21日

@author: likun
'''

import re
import urllib2
from django.http.response import HttpResponse
from django.conf import settings


class NodeAPIRedirectMiddleware(object):
    IGNORABLE_URLS = (
        re.compile(r'^/api/users/'),

    )

    def is_ignorable_request(self, request):
        self.path = request.get_full_path()
        return any(pattern.search(self.path) for pattern in self.IGNORABLE_URLS)

    def process_response(self, request, response):
        if self.is_ignorable_request(request):
            return response
        url = '{0}{1}'.format(settings.NODE_SERVER, self.path)
        req = urllib2.Request(url, headers=request.META)
        conn = urllib2.urlopen(req)

        info = conn.info()
        data = conn.read()
        return HttpResponse(data, content_type=info.get("content-type"))
