import os
from .local import DEBUG

if DEBUG:
    LOG_DIR = './logs/'
else:
    LOG_DIR = '/var/log/'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(name)s-%(levelname)s [%(filename)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[%(server_time)s] %(message)s',
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True
        },
        'service': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'service.log'),
            'formatter': 'verbose'
        },
        'auth_uuid': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'auth.log'),
            'formatter': 'verbose'
        },
        'mails': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'mails.log'),
            'formatter': 'verbose'
        },
        'celery': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'celery.log'),
            'formatter': 'verbose',
        },
        'metric': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'metric.log'),
            'formatter': 'verbose'
        },
        'website': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'website.log'),
            'formatter': 'verbose',
        },
        'accredible': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(LOG_DIR, 'accredible.log'),
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django_log': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        'service': {
            'handlers': ['service'],
            'level': 'INFO',
            'propagate': True,
        },
        'auth_uuid': {
            'handlers': ['auth_uuid'],
            'level': 'INFO',
            'propagate': True,
        },
        'mails': {
            'handlers': ['mails'],
            'level': 'INFO',
            'propagate': True,
        },
        'celery-task': {
            'handlers': ['celery', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'metric': {
            'handlers': ['metric', 'celery', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'website': {
            'handlers': ['website'],
            'level': 'INFO',
            'propagate': True,
        },
        'accredible': {
            'handlers': ['accredible'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}
