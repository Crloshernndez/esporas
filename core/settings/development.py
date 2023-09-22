from .base import *

# EMAIL
EMAIL_BACKEND       = 'djcelery_email.backends.CeleryEmailBackend'
EMAIL_HOST          = 'smtp.gmail.com'
EMAIL_PORT          = 587
EMAIL_HOST_USER     = env('USER_EMAIL_HOST')
EMAIL_HOST_PASSWORD = env('USER_EMAIL_PASSWORD')
EMAIL_USE_TLS       = True
DEFAULT_FROM_EMAIL = "info@real-estate.com"

# Database
DATABASES = {
    'default': {
        'ENGINE': env('POSTGRES_ENGINE'),
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT'),
    }
}

CELERY_BROKER_URL = env("CELERY_BROKER")
CELERY_RESULT_BACKEND = env("CELERY_BACKEND")
CELERY_TIMEZONE = 'UTC'