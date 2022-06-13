from conf.settings import *
import os

DEBUG = eval(os.environ.get("DEBUG", default=False))

TEMPLATE_DEBUG = eval(os.environ.get("DEBUG", default=False))

DATABASES = {
    'default': {
        "ENGINE": os.environ.get("SQL_ENGINE"),
        "NAME": os.environ.get("SQL_DATABASE"),
        "USER": os.environ.get("SQL_USER"),
        "PASSWORD": os.environ.get("SQL_PASSWORD"),
        "HOST": os.environ.get("SQL_HOST"),
        "PORT": os.environ.get("SQL_PORT"),
    }
}

ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8008', 'http://localhost:8008']
