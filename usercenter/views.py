# coding: utf-8
from rest_framework.views import APIView
from django.db import transaction
from django.utils.translation import gettext_lazy as _
from django.db.models import Q
from usercenter.models import User, MemberService, MemberOrder,\
    MemberOrderNotificationRecord, SubscribeSetting, Subscribe, DeivceVcode,\
    EmailEcode, UserCode, UserInvitationRecord, UserBalanceRecord
from django.contrib.auth import authenticate, login

from common.utils import random_number, md5, debug
from django.conf import settings
from rest_framework.response import Response
from usercenter.serializers import UserSerializer, MemberServiceSerializer,\
    MemberOrderSerializer, SubscribeSettingSerializer, SubscribeSerializer,\
    UserBalanceRecordSerializer
from _io import BytesIO
from common import check_code, bitpay_rates
from django.http.response import HttpResponse
from django.core.mail import send_mail
from rest_framework.generics import ListAPIView
from bitpay.bitpay_client import Client
from common.rest_utils import app_login_required, app_user, app_device,\
    app_data_required, app_member_required
from django.contrib.sites.models import Site
import time
from django.utils.timezone import now
import datetime
from string import upper, lower
from django.template.loader import render_to_string
from django.views.generic.base import View


class LoginAPIView(APIView):
    '''
    登陆
    '''
    app_data_required('username', 'password', 'vcode')

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        vcode = upper(data.get('vcode', ''))
        device = app_device(request)
        if not device:
            device = username
        dv = DeivceVcode.objects.filter(device=device).first()
        origin_vcode = dv.vcode if dv else ''
        if vcode == origin_vcode:
            try:
                user = User.objects.get(
                    Q(username=username) | Q(email=username))
                user = authenticate(username=user.username, password=password)
                if user:
                    user.token = md5(
                        '{0}{1}{2}'.format(username, random_number(6), settings.SECRET_KEY))
                    user.save()
                    login(request, user)
                    return Response(UserSerializer(user).data)
                else:
                    return Response({'code': 40001, 'detail': _(u'密码错误')})
            except User.DoesNotExist:
                return Response({'code': 40001, 'detail': _(u'用户名不存在')})
        return Response({'code': 40001, 'detail': _(u'验证码错误')})


class LoginVcodeView(APIView):
    '''
    生成图片验证码
    '''

    def get(self, request, *args, **kwargs):
        data = request.query_params.copy()
        device = app_device(request)
        if not device:
            device = data.get('username', '')
        f = BytesIO()
        img, code = check_code.create_validate_code()
        DeivceVcode.objects.update_or_create(
            device=device, defaults={'vcode': upper(code)})
        img.save(f, 'GIF')
        return HttpResponse(f.getvalue(), content_type='image/gif')


class LoginEcodeAPIView(APIView):
    '''
    获取邮箱验证码
    '''

    def get(self, request, *args, **kwargs):
        data = request.query_params.copy()
        email = data.get('email')
        ecode = random_number(4)
        EmailEcode.objects.update_or_create(
            email=email, defaults={'ecode': ecode})
        message = render_to_string('users/email.html', {'ecode': ecode})
        send_mail(u'邮件验证码 Verification Code', message, settings.SERVER_EMAIL,
                  [email, ], html_message=message)
        return Response({'code': 0, 'detail': _(u'邮件发送成功')})


class LoginCheckUsernameAPIView(APIView):
    '''
    验证用户名是否存在
    '''

    def get(self, request, *args, **kwargs):
        data = request.query_params.copy()
        username = data.get('username')
        return Response({'exists': User.objects.filter(username=username).exists()})


class LoginCheckEmailAPIView(APIView):
    '''
    验证邮箱是否存在
    '''

    def get(self, request, *args, **kwargs):
        data = request.query_params.copy()
        email = data.get('email')
        return Response({'exists': User.objects.filter(email=email).exists()})


class LoginCheckVcodeAPIView(APIView):
    '''
    验证验证码是否正确
    '''

    def get(self, request, *args, **kwargs):
        data = request.query_params.copy()
        vcode = upper(data.get('vcode', ''))
        device = app_device(request)
        if not device:
            device = data.get('username')
        dv = DeivceVcode.objects.filter(device=device).first()
        origin_vcode = dv.vcode if dv else ''
        return Response({'valid': vcode == origin_vcode})


class LoginCheckEcodeAPIView(APIView):
    '''
    验证邮箱验证码是否正确
    '''

    @app_data_required('email', 'ecode')
    def get(self, request, *args, **kwargs):
        data = request.query_params.copy()
        ecode = data.get('ecode')
        email = data.get('email')
        ec = EmailEcode.objects.filter(email=email).first()
        origin_ecode = ec.ecode if ec else ''
        return Response({'valid': ecode == origin_ecode})


class RegisterAPIView(APIView):
    '''
    用户注册
    '''
    @app_data_required('username', 'email', 'password', 'ecode')
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username')
        if User.objects.filter(username=username).exists():
            return Response({'code': 40002, 'detail': _(u'用户名已存在')})
        email = data.get('email')
        if User.objects.filter(email=email).exists():
            return Response({'code': 40002, 'detail': _(u'邮箱已存在')})
        password = data.get('password')
        ecode = data.get('ecode')
        ec = EmailEcode.objects.filter(email=email).first()
        origin_ecode = ec.ecode if ec else ''
        if ecode != origin_ecode:
            return Response({'code': 40002, 'detail': _(u'邮箱验证码错误')})

        user = User.objects.create_user(username, email, password)
        user.token = md5(
            '{0}{1}{2}'.format(username, random_number(6), settings.SECRET_KEY))
        user.save()

        # 注册邀请记录
        icode = data.get('icode')

        if icode:
            try:
                uc = UserCode.objects.get(code=icode)
                UserInvitationRecord.objects.create(user=user, inviter=uc.user)
            except UserCode.DoesNotExist:
                return Response({'code': 40002, 'detail': _(u'邀请码不存在')})
        else:
            UserInvitationRecord.objects.create(user=user)

        user = authenticate(username=username, password=password)
        login(request, user)
        return Response(UserSerializer(user).data)


class ChangePasswordAPIView(APIView):
    '''
    修改密码
    '''
    @app_login_required
    @app_data_required('old_password', 'new_password', )
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        user = request.app_user
        data = request.data
        old_password = data.get('old_password')
        if not user.check_password(old_password):
            return Response({'code': 40001, 'detail': _(u'原密码错误')})

        new_password = data.get('new_password')
        user.set_password(new_password)
        user.token = md5(
            '{0}{1}{2}'.format(user.username, random_number(6), settings.SECRET_KEY))
        user.save()
        user = authenticate(username=user.username, password=new_password)
        login(request, user)
        return Response(UserSerializer(user).data)


class MemberStatusAPIView(APIView):
    '''
    获取会员状态
    '''

    @app_login_required
    def get(self, request, *args, **kwargs):
        user = self.request.app_user
        return Response({'is_member': user.is_member, 'member_last_date': user.member_last_date, 'balance': user.balance})


class MemberServiceListAPIView(APIView):
    '''
    获取会员服务价格列表
    '''
    serializer_class = MemberServiceSerializer

    def get(self, request, *args, **kwargs):
        qs = MemberService.objects.filter(status=1).order_by('coin_type')
        objs = self.serializer_class(qs, many=True).data
        data = {}
        rate = bitpay_rates.get_usd_rate()
        for obj in objs:
            ct = obj.get('coin_type')
            arr = data.get(ct, [])
            if ct == 'BTC':
                obj.update({'coin_price': round(float(obj.get('price')) /
                                                rate, 8)})
            arr.append(obj)
            data.update({ct: arr})
        return Response({'data': data})


class MemberOrderListAPIView(ListAPIView):
    '''
    会员购买记录列表
    '''
    serializer_class = MemberOrderSerializer

    def get_queryset(self):
        user = self.request.app_user
        data = self.request.query_params.copy()
        status = data.get('status', '')
        qs = MemberOrder.objects.filter(user=user)
        if status:
            qs = qs.filter(status=status)
        return qs

    @app_login_required
    def get(self, request, *args, **kwargs):
        return ListAPIView.get(self, request, *args, **kwargs)


class MemberPaymentAPIView(APIView):
    '''
    会员购买
    '''
    @app_login_required
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        user = request.app_user
        data = request.data
        mspk = data.get('mspk')
        ms = MemberService.objects.get(pk=mspk)

        if MemberOrder.objects.filter(user=user, status__in=('new', 'paid'), created_datetime__gt=now() - datetime.timedelta(seconds=15 * 60)).exists():
            return Response({'code': 40009, 'detail': _(u'未支付或未确认订单等待处理')})
        last_date = user.member_last_date
        if last_date and now().date() <= last_date:
            start_date = last_date + datetime.timedelta(days=1)
        else:
            start_date = now().date()
        end_date = start_date + datetime.timedelta(days=ms.duration)

        price = round(float(ms.price) / bitpay_rates.get_usd_rate(), 8)
        notificationURL = '{0}/api/users/payment/callback/'.format(
            Site.objects.get_current(request).domain)
        order_id = '{0}{1}'.format(int(time.time()), random_number(4))

        client = Client(api_uri=settings.BITPAY_API_URL,
                        insecure=False, pem=settings.BITPAY_KEY)

#         print client.create_token('merchant')
#         token = client.tokens['merchant']
#         print token
        token = settings.BITPAY_TOKEN
        data = client.create_invoice({"price": price, "currency": ms.coin_type, "transactionSpeed": "medium", "fullNotifications": "true", "notificationURL":
                                      notificationURL, "buyer": {"email": user.email}, "orderId": order_id, "token": token})

        order = MemberOrder.objects.create(order_id=order_id, user=user, service=ms, guid=data.get('guid', ''), url=data.get('url'), start_date=start_date, end_date=end_date, coin_type=ms.coin_type, coin_amount=price, status=data.get(
            'status'), exception_status=data.get('exceptionStatus'), invoice_id=data.get('id'), addresses=data.get('addresses'), origin=data)
        debug('payment_data', data)
        return Response({'invoice_id': order.invoice_id, 'url': data.get('url')})


class MemberPaymentCallbackAPIView(APIView):
    '''
    会员购买状态通知
    '''

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        data = request.data
        debug('notification_url', data)
        invoice_id = data.get('id')
        status = data.get('status')
        exceptionStatus = lower(str(data.get('exceptionStatus')))
        order = MemberOrder.objects.get(invoice_id=invoice_id)
        order.status = status
        order.exception_status = exceptionStatus
        order.save()
        user = order.user
        MemberOrderNotificationRecord.objects.create(
            order=order, user=user, invoice_id=invoice_id, status=status, exception_status=exceptionStatus, origin=data)

        client = Client(api_uri=settings.BITPAY_API_URL)
        invoice_data = client.get_invoice(invoice_id)
        debug('notification_url_invoice_data', invoice_data)
        if invoice_data.get('status') == 'confirmed':  # 确认等级中
            #         if invoice_data.get('status') == 'complete'#确认等级慢
            user.is_member = True
            user.member_last_date = order.end_date
            user.save()
        return Response({'invoice_id': order.invoice_id})


class SubscribeSettingAPIView(APIView):
    '''
    订阅设置
    '''

    serializer_class = SubscribeSettingSerializer

    @app_member_required
    def get(self, request, *args, **kwargs):
        user = request.app_user
        ssg, _ = SubscribeSetting.objects.get_or_create(user=user)
        return Response(self.serializer_class(ssg).data)

    @app_member_required
    def post(self, request, *args, **kwargs):
        user = request.app_user
        ssg, _ = SubscribeSetting.objects.get_or_create(user=user)
        data = request.data
        print data
        ssg.start_time = data.get('start_time')
        ssg.end_time = data.get('end_time')
        ssg.status = data.get('status')
        ssg.save()
        return Response(self.serializer_class(ssg).data)


class SubscribeListAPIView(ListAPIView):
    '''
    订阅列表
    '''
    serializer_class = SubscribeSerializer

    def get_queryset(self):
        user = app_user(self.request)
        qs = Subscribe.objects.filter(user=user, status=1)
        return qs

    @app_member_required
    def get(self, request, *args, **kwargs):
        return super(SubscribeListAPIView, self).get(request, *args, **kwargs)


class SubscribeCancelAPIView(APIView):
    '''
    订阅取消
    '''

    @app_member_required
    @app_data_required('pk')
    def post(self, request, *args, **kwargs):
        data = request.data
        pk = data.get('pk')
        Subscribe.objects.filter(pk=pk).update(status=0)
        return Response({'code': 0, 'detail':  _(u'取消成功')})


class IosPayCheck(APIView):

    def get(self, request, *args, **kwargs):
        return Response({'show': settings.IOS_PAY_SHOW})


class UserInvitationAPIView(APIView):
    '''
    用户邀请码，邀请链接
    '''
    @app_login_required
    def get(self, request, *args, **kwargs):
        user = request.app_user
        uc, _ = UserCode.objects.get_or_create(user=user)
        return Response({'icode': uc.code, 'link': uc.link})


class UserBalanceListAPIView(ListAPIView):
    '''
    余额变化列表
    '''
    serializer_class = UserBalanceRecordSerializer

    def get_queryset(self):
        user = self.request.app_user
        return UserBalanceRecord.objects.filter(user=user)

    @app_login_required
    def get(self, request, *args, **kwargs):
        return super(UserBalanceListAPIView, self).get(request, *args, **kwargs)
