# coding: utf-8
from django.utils.translation import gettext_lazy as _
"""
Django settings for blockcashflow project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_abs(path):
    return os.path.join(BASE_DIR, path)


import sys
reload(sys)
sys.setdefaultencoding('utf-8')
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'n*p#-&dre7f#-yuyg=vz%p%9g8%8y2e$_49vm5jax8yur@mzrq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ADMINS = (('likun', 'likun@xin-shui.com'), ('lishaojie', 'lisj@xin-shui.com'),)
EMAIL_SUBJECT_PREFIX = '[500 ERROR FOR ADMIN]'
EMAIL_HOST = 'imap-mail.outlook.com'
EMAIL_PORT = 993
SERVER_EMAIL = 'blockcashflow@outlook.com'
EMAIL_HOST_USER = SERVER_EMAIL
EMAIL_HOST_PASSWORD = 'BBbb5678'
EMAIL_USE_TLS = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'debug_toolbar',
    'djcelery',
    'rest_framework',
    'common',
    'usercenter',
    'investment',
    'notification',
    'blockchain_db',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'common.middleware.NodeAPIRedirectMiddleware',
)
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]
DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': "/static/js/jquery.min.js"
}
INTERNAL_IPS = ['127.0.0.1', ]
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    '*'
)
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)
CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)

ROOT_URLCONF = 'blockcashflow.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blockcashflow.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blockcashflow',
        'HOST': 'rm-2ze2ytva34g5604dho.mysql.rds.aliyuncs.com',
        'PORT': 3306,
        'USER': 'xs_test_user',
        'PASSWORD': 'AAaa1231'
    },
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh_CN'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    get_abs('static'),
)

AUTH_USER_MODEL = 'usercenter.User'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': get_abs('logs/debug.log'),
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'debug': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
        }
    }
}

# django_sult config
SUIT_CONFIG = {
    'ADMIN_NAME': _(u'blockcashflow后台管理'),

    'MENU_ICONS': {
        'sites': 'icon-leaf',
    },
    'LIST_PER_PAGE': 100,
    'MENU': (
        'sites',
        {'app': 'usercenter', 'label': _(u'用户中心'), 'icon': 'icon-star'},
        {'app': 'investment', 'label': _(u'智能预测'), 'icon': 'icon-star'},
        {'app': 'notification', 'label': _(u'消息推送'), 'icon': 'icon-envelope'},
        {'app': 'djcelery', 'label': _(u'定时任务'), 'icon': 'icon-bell'},
        {'label': _(u'系统用户设置'), 'icon': 'icon-cog',
         'models': ('auth.group',)},
    )
}
import djcelery
djcelery.setup_loader()
# djcelery+broker配置
BROKER_URL = 'redis://:redis7890@127.0.0.1:6379/1'
CELERY_RESULT_BACKEND = 'redis://:redis7890@127.0.0.1:6379/1'
REDIS_CONNECT_RETRY = True
CELERY_TASK_RESULT_EXPIRES = 10
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
SOUTH_MIGRATION_MODULES = {
    'djcelery': 'djcelery.south_migrations',
}

CELERY_TIMEZONE = TIME_ZONE

BITPAY_API_URL = 'https://bitpay.com'
BITPAY_KEY = '''
-----BEGIN EC PRIVATE KEY-----
MHQCAQEEID53OR04BMVEZHIXWDBG7XWN3CeojiVIkSNy26wqonsdoAcGBSuBBAAK
oUQDQgAEc/dzbPAQUgOP2TsokE6OZinzUWxD7wOQy1SclqGERlYp+Lj3ZlWREkaF
VrnCEbAUZOfBHdvfog+2oEDHyrbCAg==
-----END EC PRIVATE KEY-----
'''
BITPAY_TOKEN = 'CkLUWfWY7QkpybQvRv9xVdDvUDZGfcjnTbuRxNfmg9tF'

IOS_PAY_SHOW = True

NODE_SERVER = 'http://127.0.0.1:5000'

URLSCHEME = 'blockcashflow://app/'

ALI_ACCESSKEYID = 'LTAIADUkOv5ReEKC'
ALI_ACCESSKEYSECRET = 'NI0I6Gk7FzW1Bi0b1yIcQkCMqnBXya'
ALI_REGIONID = 'cn-hangzhou'
ALI_APPKEY = '24855419'

REGISTER_AMOUNT = 1000.0
INVITATION_REGISTER_AMOUNT = 2000.0
INVITATION_AMOUNT = 1000.0
BCF_RATE = 0.015625
INVITATION_MAX_AMOUNT = 100000.0
