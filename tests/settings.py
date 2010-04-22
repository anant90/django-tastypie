import os

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

MEDIA_ROOT = os.path.normpath(os.path.join(BASE_PATH, 'media'))

DATABASE_ENGINE = 'sqlite3'
DATABASE_NAME = 'tastypie.db'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'tastypie',
]

DEBUG = True
TEMPLATE_DEBUG = DEBUG
