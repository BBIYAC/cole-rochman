# prod.py 파일은 실제 서비스를 위한 운영 코드

from .base import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

DEBUG = True

ALLOWED_HOSTS = secrets.get('ALLOWED_HOST')

DATABASES = {
    'default': secrets.get('DB_SETTINGS')#.get('TEST')
}

# noinspection PyUnresolvedReferences

STATIC_ROOT = '/var/www/cole-rochman/static'

sentry_sdk.init(
    dsn=secrets.get('SENTRY_ADDRESS'),
    integrations=[DjangoIntegration()],
    environment='production'
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s SENDER_NAME PROGRAM_NAME: %(message)s',
            'datefmt': '%Y-%m-%dT%H:%M:%S',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(PROJECT_DIR, 'settings/debug.log'),
        },
        'console': {
            'class': 'logging.StreamHandler',
        },
        'SysLog': {
            'level': 'DEBUG',
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'simple',
            'address': secrets.get('PAPERTRAIL_ADDRESS')
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file', 'SysLog'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

BROKER_URL = secrets.get('BROKER_URL')

AUTO_SEND_NOTIFICAITON = True
