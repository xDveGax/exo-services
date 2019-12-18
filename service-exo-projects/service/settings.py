"""
Django settings for service project.
"""
import os
import sys
import sentry_sdk

from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.redis import RedisIntegration

from .local import *  # noqa
from .apps import INSTALLED_APPS as PROJECT_APPS  # noqa
from .logging import LOGGING  # noqa
from .jwt_settings import *  # noqa
from .settings_populate import *  # noqa

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEST_MODE = sys.argv[1:2] == ['test']
BRAND_NAME = 'OpenExO'
SERVICE_SHORT_NAME = SERVICE_NAME.split('-')[-1]  # noqa

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', '(@ld*aiy5419but+akxofqmng1_p8c(57w1772hnoe58ydui^7')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'auth_uuid.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'service.urls'
INSTALLED_APPS = PROJECT_APPS     # noqa

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_RENDERER_CLASSES': (
        'djangorestframework_camel_case.render.CamelCaseJSONRenderer',
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PARSER_CLASSES': [
        'djangorestframework_camel_case.parser.CamelCaseJSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
    ],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
    'TEST_REQUEST_RENDERER_CLASSES': (
        'rest_framework.renderers.MultiPartRenderer',
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.TemplateHTMLRenderer'
    ),
    'DEFAULT_PAGINATION_CLASS': 'utils.drf.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}

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

WSGI_APPLICATION = 'service.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATIC_URL = os.path.join(FORCE_SCRIPT_NAME or '', '/static/')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Auth

LOGIN_URL = '/admin'

# User image sizes

SMALL_IMAGE_SIZE = 24
MEDIUM_IMAGE_SIZE = 48
LARGE_IMAGE_SIZE = 96
DEFAULT_IMAGE_SIZE = 144

# Sendgrid settings

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Faker
FAKER_SETTINGS_LOCALE = 'en_GB'

SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS = {
    'host': REDIS_HOST,
    'port': REDIS_PORT,
    'db': REDIS_AUTH_DB,
    'prefix': 'session',
    'socket_timeout': 1,
    'retry_on_timeout': False
}

AUTH_USER_MODEL = 'auth_uuid.UserUUID'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',  # default
    'guardian.backends.ObjectPermissionBackend',
)
URL_VALIDATE_USER_COOKIE = '{}/{}'.format(EXOLEVER_HOST, 'api/accounts/me/')
AUTH_SECRET_KEY = os.environ.get('AUTH_SECRET_KEY', 'o134467ss##w@kusnw@)1d2uu%#blvj!+1ej6obgc@%q=wr)&4')
INTERNAL_REDIRECT = 'internal_redirect'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

ANONYMOUS_USER_ID = None
ANONYMOUS_USER_NAME = None
GUARDIAN_MONKEY_PATCH = False

CELERY_SERVICE_RESULT_BACKEND = 'django-db'
CELERY_SERVICE_BROKER_URL = 'redis://{}:{}/{}'.format(REDIS_HOST, REDIS_PORT, REDIS_CELERY_DB)

FILES_USER_SERIALIZER = 'utils.drf.user.UserSerializer'

HEALTH_CHECK = {
    'DISK_USAGE_MAX': 90,  # percent
    'MEMORY_MIN': 100,    # in MB
}

if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        environment=SENTRY_ENV,
        release=SENTRY_VER,
        integrations=[
            DjangoIntegration(),
            CeleryIntegration(),
            RedisIntegration(),
        ]
    )

if DEBUG:
    from .debug import *  # noqa

if TEST_MODE:
    from .settings_test_override import *   # noqa

if POPULATOR_MODE:
    from .settings_populate_override import *  # noqa
