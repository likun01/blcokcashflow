# coding: utf-8
import logging
import random
import hashlib
import datetime
import time
import qrcode
import StringIO
import base64

from django.db.models.expressions import Func
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from django.conf import settings


def debug(token, info, error=False):
    logger = logging.getLogger('debug')
    tag = '#' if error else '-'
    logger.info(token.center(50, tag))
    if error:
        logger.error(info)
    else:
        logger.info(info)
    logger.info(token.center(50, tag))


def avg(iterator):
    if iterator:
        return float(sum(iterator)) / (len(iterator) * 1.0)
    return 0


def avg_ignore_zero(iterator):
    if iterator:
        count = 0
        num_sum = 0
        for num in iterator:
            if num != 0:
                num_sum += num
                count += 1
        if count != 0:
            return num_sum / (count * 1.0)
    return 0


class Replace(Func):
    function = 'REPLACE'
    template = '%(function)s(%(expressions)s, " ", "")'


class NullIfZero(Func):
    function = 'NULLIF'
    template = '%(function)s(%(expressions)s, 0)'


def random_number(n):
    rand = map(lambda x: str(x), range(0, 10))
    return ''.join(random.sample(rand, n))


def md5(s):
    md5 = hashlib.md5()
    md5.update(s)
    return md5.hexdigest()


def datetime2timestamp(dt):
    if isinstance(dt, (datetime.datetime, datetime.date)):
        return long(time.mktime(dt.timetuple()))
    return dt


def datetime2microsecond(dt):
    if isinstance(dt, datetime.datetime):
        seconds = long(time.mktime(dt.timetuple()))
        return long(seconds * 1000 + dt.microsecond / 1000)
    if isinstance(dt, datetime.date):
        return long(time.mktime(dt.timetuple())) * 1000
    return dt


def microsecond2date(ts):
    if isinstance(ts, int):
        return datetime.datetime.fromtimestamp(ts / 1000.0).date()
    return ts


def buildqrcode(code):
    '''
    生成225x225二维码的base64
    '''
    qr = qrcode.QRCode(
        version=5,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=5,
        border=4,
    )
    qr.add_data(code)
    qr.make(fit=True)
    img = qr.make_image()
    output = StringIO.StringIO()
    img.save(output)
    contents = output.getvalue()
    output.close()
    b64 = 'data:image/png;base64, {0}'.format(base64.b64encode(contents))
    return b64


def number_human(value):
    format_value = u'{0:.1f}'.format(value)
    if value >= 10**8 or value <= -10**8:
        format_value = u'{0:.2f}亿'.format(value / 100000000.0)
    elif value >= 10**4 or value <= -10**4:
        format_value = u'{0:.1f}万'.format(value / 10000.0)
    return format_value


def hide_address(address):
    if address:
        return '{0}{1}'.format(address[:4], (len(address) - 4) * '*')
    return ''


def coin_name(coin):
    coin_choices = {'BTC': u'比特币', 'LTC': u'莱特币'}
    if coin in coin_choices:
        return coin_choices.get(coin)
    return coin


def send_mail_files(subject, recipient_list, files):
    sender = settings.SERVER_EMAIL

    smtpserver = settings.EMAIL_HOST
    username = settings.EMAIL_HOST_USER
    password = settings.EMAIL_HOST_PASSWORD

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject

    for path in files:
        # 构造附件
        fname = path.split('/')[-1]
        att = MIMEText(open(path, 'rb').read(), 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename="{}"'.format(fname)
        msgRoot.attach(att)

    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    smtp.sendmail(sender, recipient_list, msgRoot.as_string())
    smtp.quit()
