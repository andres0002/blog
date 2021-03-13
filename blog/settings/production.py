from blog.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['blogappwebandres.herokuapp.com']

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd60kuht9749l35',
        'USER': 'yweqpcnpwdngqn',
        'PASSWORD': 'ad17e0db46a139f566a5fc2c2eb4340ee6a226d8380d670f989c30f3d47bb992',
        'HOST': 'ec2-54-145-249-177.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}