from .base import *

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Akash',
        'USER': 'postgres',
        'PASSWORD': 'Nikhil@123',
        'HOST': 'localhost',
    }
}

