from .tajna import *
from .url_prefix import *
import datetime
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
MEDIA_DIR = os.path.join(BASE_DIR, 'media')

SECRET_KEY = 'v2l3&kn(0p*d)kr_0c-=$_#(v%lt@0nt^vz31$27w#99-ej8_w'
DEBUG = True
ALLOWED_HOSTS = ['*']

# E-mail postavke
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Bez ovoga, django-rest-auth ne dela!
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # 'Prava' e-poštanska infrastruktura.
DEFAULT_FROM_EMAIL = 'hvk@koris.hr'
EMAIL_HOST = 'mail.koris.hr'
EMAIL_PORT = 25
EMAIL_HOST_USER = 'hvk@koris.hr'
EMAIL_USE_TLS = True

INSTALLED_APPS = [
    'suit',  # Mora biti prije admina.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_filters',  # !!!
    'kat.apps.KatConfig',
    'hvk.apps.HvkConfig',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',

    'sim.apps.SimConfig',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'k2_ws.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': True,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',  # Za uključivanje rada sa slikama i multimedijom.
            ],
        },
    },
]

WSGI_APPLICATION = 'k2_ws.wsgi.application'
STATIC_URL = '{0}/static/'.format(URL_PREFIX)
# STATICFILES_DIRS = [STATIC_DIR, ]
MEDIA_ROOT = MEDIA_DIR
STATIC_ROOT = STATIC_DIR
MEDIA_URL = '{0}/media/'.format(URL_PREFIX)

# DATABASES podaci su u tajni. ;-)

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]

LANGUAGE_CODE = 'hr-hr'
TIME_ZONE = 'Europe/Zagreb'
USE_I18N = True
USE_L10N = True
USE_TZ = True

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': 'HVK admin',
    'HEADER_DATE_FORMAT': 'Y-m-d',
    'HEADER_TIME_FORMAT': 'H:i',

    # forms
    # 'SHOW_REQUIRED_ASTERISK': True,  # Default True
    # 'CONFIRM_UNSAVED_CHANGES': True, # Default True

    # menu
    # 'SEARCH_URL': '/admin/auth/user/',
    # 'MENU_ICONS': {
    #    'sites': 'icon-leaf',
    #    'auth': 'icon-lock',
    # },
    'MENU_OPEN_FIRST_CHILD': False,  # Default True
    # 'MENU_EXCLUDE': ('auth.group',),
    # 'MENU': (
    #     'sites',
    #     {'app': 'auth', 'icon':'icon-lock', 'models': ('user', 'group')},
    #     {'label': 'Settings', 'icon':'icon-cog', 'models': ('auth.user', 'auth.group')},
    #     {'label': 'Support', 'icon':'icon-question-sign', 'url': '/support/'},
    # ),

    # misc
    # 'LIST_PER_PAGE': 15
}

HVK_CLAN_FOTO_PATH = 'hvk_clanovi'
HVK_CLAN_FOTO_WIDTH = '100em'
HVK_PRAZAN_DAT_DO = '...'
HVK_AUTOCOMPLETE_RECORD_COUNT = 10

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',  # Za autentikaciju 'običnim' DRF tokenom.
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',  # Za autentikaciju JSOn web-tokenom.
        'rest_framework.authentication.SessionAuthentication',  # Za korištenje Browsable API-ja uz autentikaciju tokenom.
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # OVAJ PARAMETAR RAZJEBAVA WEB-API!
    # 'PAGE_SIZE': 10,
    'EXCEPTION_HANDLER': 'hvk.exceptions.handle_exception'
}

# REST AUTH
SITE_ID = 1  # Za registraciju pomoću django-rest-auth.
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'hvk.serializers.HVKRegSerializr',
}

# REST AUTH JWT
REST_USE_JWT = True
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(hours=1),
    'JWT_ALLOW_REFRESH': True,
}

# CORS, vidi: https://stackoverflow.com/questions/35760943/how-can-i-enable-cors-on-django-rest-framework#35761088
CORS_ORIGIN_ALLOW_ALL = True
