# coding: utf-8
'''
Created on 2018年3月27日

@author: likun
'''
from notification.aliyun import ALiYunSdk


class PushSdk(object):

    def __init__(self):
        self.ali_sdk = ALiYunSdk()

    def _push_to_aliyun(self, devicetype, tag, title, content, urlscheme):
        return self.ali_sdk.publish(
            devicetype, tag, title, content, urlscheme)

    def publish(self, devicetype, tag, title, content, urlscheme):
        '''
        devicetype: 设备类型

        '''
        if devicetype == 'all':
            res1, msg1 = self._push_to_aliyun(
                'ANDROID', tag, title, content, urlscheme)
            res2, msg2 = self._push_to_aliyun(
                'iOS', tag, title, content, urlscheme)
            res = res1 and res2
            msg = '_'.join([msg1, msg2])
        else:
            res, msg = self._push_to_aliyun(
                devicetype, tag, title, content, urlscheme)

        return res, msg

    def publish_to_alias(self, alias, title, content, urlscheme):
        return self.ali_sdk.publish_to_alias(alias, title, content, urlscheme)

    def publish_to_alias_batch(self, aliases, title, content, urlscheme):
        res, msg = self.ali_sdk.publish_to_alias_batch(
            aliases, title, content, urlscheme)
        return res, msg
