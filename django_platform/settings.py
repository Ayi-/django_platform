"""
Django settings for django_platform project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from django.conf import settings
from django.conf.urls.static import static


from os import environ
debug = not environ.get("APP_NAME", "") 

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_!#%pvc2%0r8et8!4ua4&*m(6wg1yc8hbxygz30!+go)hv0-ca'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'app',
    'django_jinja',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'django_platform.urls'

TEMPLATES = [
    # {
    #     "BACKEND": "django.template.backends.jinja2.Jinja2",
    #     'DIRS': [
    #         'app/templates',
    #     ],
    #     "APP_DIRS": True,
    #     "OPTIONS":{
    #         "autoescape": True,
    #     "auto_reload": settings.DEBUG,
    #     },
    #
    # },
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        'DIRS': [
            os.path.join(BASE_DIR, 'app/jinja2'),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            # Match the template names ending in .html but not the ones in the admin folder.
            "match_extension": ".html",
            #"match_regex": r"^(?!admin/).*",
            "app_dirname": os.path.join(BASE_DIR, 'app'),

            # Can be set to "jinja2.Undefined" or any other subclass.
            "undefined": None,

            "newstyle_gettext": True,

            "extensions": [
                "jinja2.ext.do",
                "jinja2.ext.loopcontrols",
                "jinja2.ext.with_",
                "jinja2.ext.i18n",
                "jinja2.ext.autoescape",
                "django_jinja.builtins.extensions.CsrfExtension",
                "django_jinja.builtins.extensions.CacheExtension",
                "django_jinja.builtins.extensions.TimezoneExtension",
                "django_jinja.builtins.extensions.UrlsExtension",
                "django_jinja.builtins.extensions.StaticFilesExtension",
                "django_jinja.builtins.extensions.DjangoFiltersExtension",
            ],
            "autoescape": True,
            "auto_reload": settings.DEBUG,
            "translation_engine": "django.utils.translation",
        }
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },




]

WSGI_APPLICATION = 'django_platform.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


if debug:

    MYSQL_DB = 'djangopl'    
    MYSQL_USER = 'root' 
    MYSQL_PASS = '0000' 
    MYSQL_HOST_M = '127.0.0.1' 
    MYSQL_HOST_S = '127.0.0.1' 
    MYSQL_PORT = '3306' 
else: 
#SAE 
    import sae.const 
    MYSQL_DB = sae.const.MYSQL_DB 
    MYSQL_USER = sae.const.MYSQL_USER 
    MYSQL_PASS = sae.const.MYSQL_PASS 
    MYSQL_HOST_M = sae.const.MYSQL_HOST 
    MYSQL_HOST_S = sae.const.MYSQL_HOST_S 
    MYSQL_PORT = sae.const.MYSQL_PORT

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': MYSQL_DB,
        'USER': MYSQL_USER,
        'PASSWORD': MYSQL_PASS,
        'HOST': MYSQL_HOST_M,
        'PORT': MYSQL_PORT,

    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'  #
#TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

# set for the @login_required
LOGIN_URL = '/login/'
AUTHENTICATION_BACKENDS = (
    'app.models.MyCustomBackend',
'django.contrib.auth.backends.ModelBackend',

)