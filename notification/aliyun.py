# coding: utf-8
'''
Created on 2018年3月27日

@author: likun
'''

from django.conf import settings
from aliyunsdkpush.request.v20160801 import PushRequest
from aliyunsdkcore import client
from common.utils import debug
import json


class ALiYunSdk():

    def __init__(self):
        self.accessKeyId = settings.ALI_ACCESSKEYID
        self.accessKeySecret = settings.ALI_ACCESSKEYSECRET
        self.regionId = settings.ALI_REGIONID
        self.appKey = settings.ALI_APPKEY

    def _push(self, devicetype, target, targetvalue, title, content, urlscheme):
        clt = client.AcsClient(
            self.accessKeyId, self.accessKeySecret, self.regionId)
        title = title[:20]
        xm_title = title[:15]
        xm_content = content[:127]

        request = PushRequest.PushRequest()
        request.set_AppKey(self.appKey)
        # 推送目标: DEVICE:按设备推送 ALIAS : 按别名推送 ACCOUNT:按帐号推送  TAG:按标签推送; ALL: 广播推送
        request.set_Target(target)
        # 根据Target来设定，如Target=DEVICE, 则对应的值为 设备id1,设备id2. 多个值使用逗号分隔.(帐号与设备有一次最多100个的限制)
        request.set_TargetValue(targetvalue)
        # 设备类型 ANDROID iOS ALL
        request.set_DeviceType(devicetype)
        # 消息类型 MESSAGE NOTICE
        request.set_PushType("NOTICE")

        extra_dict = {'urlscheme': urlscheme}
        # 消息的标题
        request.set_Title(title.encode('utf-8'))
        # 消息的内容
        request.set_Body(content.encode('utf-8'))

        # iOS配置
        request.set_iOSBadge(1)
        # 开启静默通知
        request.set_iOSSilentNotification(False)
        # iOS通知声音
        request.set_iOSMusic("default")
        # iOS的通知是通过APNs中心来发送的，需要填写对应的环境信息。"DEV" : 表示开发环境 "PRODUCT" : 表示生产环境
        request.set_iOSApnsEnv("PRODUCT")
        # 消息推送时设备不在线（既与移动推送的服务端的长连接通道不通），则这条推送会做为通知，通过苹果的APNs通道送达一次。注意：离线消息转通知仅适用于生产环境
        request.set_iOSRemind(True)
        # iOS消息转通知时使用的iOS通知内容，仅当iOSApnsEnv=PRODUCT && iOSRemind为true时有效
        request.set_iOSRemindBody("iOSRemindBody")
        # 自定义的kv结构,开发者扩展用 针对iOS设备
        request.set_iOSExtParameters(json.dumps(extra_dict))

        # android配置

        # 指定notificaitonchannel id
        request.set_AndroidNotificationChannel("1")

        # 通知的提醒方式 "VIBRATE" : 震动 "SOUND" : 声音 "BOTH" : 声音和震动 NONE : 静音
        request.set_AndroidNotifyType("SOUND")
        # 通知栏自定义样式1-100
        request.set_AndroidNotificationBarType(1)
        # 点击通知后动作 "APPLICATION" : 打开应用 "ACTIVITY" : 打开AndroidActivity "URL" : 打开URL "NONE" : 无跳转
        request.set_AndroidOpenType("ACTIVITY")
        # Android收到推送后打开对应的url,仅当AndroidOpenType="URL"有效
#         request.set_AndroidOpenUrl("www.aliyun.com")
        # 设定通知打开的activity，仅当AndroidOpenType="Activity"有效
        request.set_AndroidActivity(
            "com.blockcashflow.app.main.MainActivity")
        # Android通知声音
        request.set_AndroidMusic("default")
        # 设置该参数后启动小米托管弹窗功能, 此处指定通知点击后跳转的Activity（托管弹窗的前提条件：1. 集成小米辅助通道；2. StoreOffline参数设为true）
        request.set_AndroidXiaoMiActivity(
            "com.blockcashflow.app.main.MainActivity")
        # 设定通知的扩展属性。(注意 : 该参数要以 json map 的格式传入,否则会解析出错)
        request.set_AndroidExtParameters(json.dumps(extra_dict))

        request.set_AndroidXiaoMiNotifyTitle(xm_title.encode('utf-8'))
        request.set_AndroidXiaoMiNotifyBody(xm_content.encode('utf-8'))

        request.set_StoreOffline(True)

        try:
            debug(
                'aliyun_push_data', ', '.join([target, targetvalue, title, content, urlscheme]))
            result = clt.do_action_with_exception(request)
            result = json.loads(result)
            debug('aliyun_push', result)
            return True, result.get('MessageId')
        except Exception as e:
            debug('aliyun_push_error', e, True)
            return False, str(e)

    def publish(self, devicetype, tag, title, content, urlscheme):
        return self._push(
            devicetype, 'TAG', tag, title, content, urlscheme)

    def publish_to_alias(self, alias, title, content, urlscheme):
        return self._push('ALL', 'ALIAS', alias, title, content, urlscheme)

    def publish_to_alias_batch(self, aliases, title, content, urlscheme):
        return self._push('ALL', 'ALIAS', ','.join(aliases), title, content, urlscheme)
