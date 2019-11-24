from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'colerochman_dev',
        'USER': 'colerochman',
        'PASSWORD': 'colerochman',
        'PORT': 5432,
        'TEST': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'colerochman_test',
            'USER': 'colerochman',
            'PASSWORD': 'colerochman',
            'PORT': 5432,
        },
    },
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': os.path.join(PROJECT_DIR, 'settings/debug.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

BROKER_URL = 'redis://localhost:6380/0'

NCLOUD = secrets['NCLOUD']
BIZ_MESSAGE = {
    'CLIENT_ID': '',
    'API_KEY': '',
    'CALLBACK_NUMBER': '',
    'PLUS_FRIEND_ID': '',
    'SERVICE_ID': ''
}
