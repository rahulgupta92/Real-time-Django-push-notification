"""
Django settings for realtime_notifications project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

TEMPLATE_PATH = os.path.join(BASE_DIR,'templates')

STATIC_PATH=os.path.join(BASE_DIR,'static')

DATABASE_PATH=os.path.join(BASE_DIR,'listing.db')

LOGIN_URL='/listing/login/'
MEDIA_URL="/media/"
STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
TEMPLATE_DIRS=(
    #'/home/ht/projects/classifiedsystem/templates',

    TEMPLATE_PATH,
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'eecp@6i3jtkwnojw22qp(%yj_qvm24u3g8=&%$h6!t86fl5g6m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
# 'django.contrib.sessions',
    'user_sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notifications',
    'rn',
)

MIDDLEWARE_CLASSES = (
# 'django.contrib.sessions.middleware.SessionMiddleware',
    'user_sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'realtime_notifications.urls'

WSGI_APPLICATION = 'realtime_notifications.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


SESSION_ENGINE = 'user_sessions.backends.db'