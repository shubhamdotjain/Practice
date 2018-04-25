#!/usr/bin/env python3
#
# Copyright 2016 Red Hat, Inc.
#
# Authors:
#     Fam Zheng <famz@redhat.com>
#
# This work is licensed under the MIT License.  Please see the LICENSE file or
# http://opensource.org/licenses/MIT.

"""
Django settings for patchew project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VERSION = open(os.path.join(BASE_DIR, "VERSION"), "r").read().strip()

MODULE_DIR = os.path.join(BASE_DIR, "mods")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@f-l5@70om7o(7rda^oxd$f#60g3jy#&m^p7z@vkf+&$*@%!^o'

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'api.apps.ApiConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'URL_FIELD_NAME': 'resource_uri',
    'PAGE_SIZE': 50,
    'UPLOADED_FILES_USE_URL': True,
}

ROOT_URLCONF = 'patchew.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "www", "templates"),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': [
                'patchew.tags',
            ],
        },
    },
]

WSGI_APPLICATION = 'patchew.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

def env_detect():
    if "PATCHEW_DATA_DIR" in os.environ:
        # Docker deployment
        return False, os.environ.get("PATCHEW_DATA_DIR")
    elif "OPENSHIFT_DATA_DIR" in os.environ:
        # OpenShift deployment
        return False, os.environ.get("OPENSHIFT_DATA_DIR")
    elif "VIRTUAL_ENV" in os.environ or os.environ.get("PATCHEW_DEBUG", False):
        # Development setup
        return True, os.path.join(os.environ.get("VIRTUAL_ENV",
                                                 "/var/tmp/patchew-dev"),
                                  "data")
    elif os.environ.get("PATCHEW_TEST"):
        # Test environment
        return True, os.environ.get("PATCHEW_TEST_DATA_DIR")
    else:
        raise Exception("Unknown running environment")

DEBUG, DATA_DIR = env_detect()

# In production environments, we run in a container, behind nginx, which should
# filter the allowed host names. So be a little flexible here
ALLOWED_HOSTS = ["*"]

if not os.path.isdir(DATA_DIR):
    os.makedirs(DATA_DIR)

BLOB_DIR = os.path.join(DATA_DIR, "blob")
if not os.path.isdir(BLOB_DIR):
    os.mkdir(BLOB_DIR)

if DEBUG:
    INSTALLED_APPS += ['debug_toolbar']
    MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

MEDIA_ROOT = os.path.join(DATA_DIR, "media")
MEDIA_URL = "/media/"

if not os.path.isdir(MEDIA_ROOT):
    os.makedirs(MEDIA_ROOT)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DATA_DIR, "patchew-db.sqlite3"),
    }
}

# If the PATCHEW_ADMIN_EMAIL env var is set, let Django send error reporting to
# the address.
admin_email = os.environ.get("PATCHEW_ADMIN_EMAIL")
if admin_email:
    ADMINS = [('admin', admin_email)]

SERVER_EMAIL = 'server@patchew.org'

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'wsgi', 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

INTERNAL_IPS = [
    "127.0.0.1",
]

if not DEBUG:
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': os.path.join(DATA_DIR, "log", "patchew.log"),
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
