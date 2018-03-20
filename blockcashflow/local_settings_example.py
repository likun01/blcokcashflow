from blockcashflow.settings import *

DEBUG = True

SITE_REDIS_TIMEOUT = 1
SITE_ID = 1

MEDIA_URL = '/files/'
MEDIA_ROOT = BASE_DIR + '/data/development/files/'

MEDIA_URL = '/media/'
MEDIA_ROOT = "/home/likun/data/media/"

STATIC_ROOT = '/home/likun/data/static/'

STATICFILES_DIRS = STATICFILES_DIRS + (
    '/home/likun/env/lib/python2.7/site-packages/django/contrib/admin/static/',
)

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
SITE_REDIS_TIMEOUT = 6

REST_FRAMEWORK = {
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': ("%Y-%m-%d %H:%M:%S"),
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.TokenAuthentication',),
    'DEFAULT_PAGINATION_CLASS': 'common.rest_utils.UnquotePageNumberPagination',
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_PERMISSION_CLASSES': (
    ),
}

BITPAY_API_URL = 'https://test.bitpay.com'
BITPAY_KEY = '''
-----BEGIN EC PRIVATE KEY-----
MHQCAQEEID53OR04BMVEZHIXWDBG7XWN3CeojiVIkSNy26wqonsdoAcGBSuBBAAK
oUQDQgAEc/dzbPAQUgOP2TsokE6OZinzUWxD7wOQy1SclqGERlYp+Lj3ZlWREkaF
VrnCEbAUZOfBHdvfog+2oEDHyrbCAg==
-----END EC PRIVATE KEY-----
'''
BITPAY_TOKEN = 'AKANEv6RBiK69xGp2heFz8dHSPGxT4z8eSUNT6R24j2P'
