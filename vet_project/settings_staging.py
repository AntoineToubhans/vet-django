from vet_project.settings import *

DEBUG = False
ALLOWED_HOSTS = ['52.14.42.220', 'vet.toubhans.org']

DATABASES = {
 'default': {
     'ENGINE': 'django.db.backends.postgresql',
     'NAME': 'postgres',
     'USER': 'postgres',
     'PASSWORD': 'postgres',
     'HOST': 'localhost',
     'PORT': 5432,
 }
}


# Media files
MEDIA_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../media'))


# Logging
LOG_ROOT = os.path.abspath(os.path.join(BASE_DIR, '../logs'))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'applogfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_ROOT, 'portail_rg.log'),
            'maxBytes': 1024*1024*15,  # 15MB
            'backupCount': 5,
        },
    },
    'loggers': {
        'django': {
            'handlers':['applogfile'],
            'propagate': True,
            'level': 'DEBUG',
        },
        'api': {
            'handlers': ['applogfile',],
            'level': 'DEBUG',
        },
    }
}
