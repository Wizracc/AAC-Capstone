"""
Django settings for AACForm project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os, sys
import dotenv
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

SECRET_KEY = os.environ["SECRET_KEY"]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['.herokuapp.com','localhost','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'makeReports',
    'bootstrap4',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gdstorage',
    'django_summernote',
    'rest_framework',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AACForm.urls'

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

WSGI_APPLICATION = 'AACForm.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'dec475dtrh1d4b',                      
#         'USER': 'npaddmsaelzkwn',
#         'PASSWORD': '35536c3e563d2356d340584ccdc300cd67bb7e311f86408872183b955b4bb2ff',
#         'HOST': 'ec2-107-21-98-89.compute-1.amazonaws.com',
#         'PORT': '5432',
#     } 
# }
DATABASES = {}
DATABASES["default"] = dj_database_url.config(conn_max_age=600)

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
TEST_DATABASES = {
    'default': dj_database_url.parse(os.environ["TEST_DATABASE_URL"], conn_max_age=600)
}

# Use when wanting PostgreSQL database
TEST_RUNNER =  "makeReports.tests.test_suite_runner.HerokuTestSuiteRunner"

LOGIN_REDIRECT_URL="/"
# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'


f = open(os.path.join(BASE_DIR,'gd_cred2.json'),'w')
f.write(os.environ['GD_KEY'])
f.close()

GOOGLE_DRIVE_STORAGE_JSON_KEY_FILE= os.path.join(BASE_DIR,'gd_cred2.json')
DEFAULT_FILE_STORAGE = "gdstorage.storage.GoogleDriveStorage"
SUMMERNOTE_THEME = 'bs4'
SUMMERNOTE_CONFIG = {
    'summernote': {
        # As an example, using Summernote Air-mo
        # Change editor size
        'style':'width:500px;height:750px;'
    },

    # Set custom storage class for attachments.
    'toolbar': [
        ['cleaner',['cleaner']],
        ['style',['style']],
        ['font',['bold','italic','underline','clear']],
        ['color',['color']],
        ['para',['ul','ol','paragraph']],
        ['height',['height']],
        ['table',['table']],
        ['insert',['link','hr']],
        ['view',['fullscreen','codeview']],
    ],
    # To use external plugins,
    # Include them within `css` and `js`.
    'js': (
        os.path.join(STATIC_URL, 'extPlugin/summernote-cleaner.js'),
    )
}

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication'
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ]
}