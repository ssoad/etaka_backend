"""
Django settings for django_sms_auth project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
AUTH_USER_MODEL = 'accounts.User'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-r2#44o@o$obed@p-vzu!hrqh@^-b211=sj#_4$bs1$7hsdmty3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','ssoad.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    "phone_verify",
    'accounts.apps.AccountsConfig',
    'transactions.apps.TransactionsConfig'
]
REST_FRAMEWORK = {
     'DEFAULT_AUTHENTICATION_CLASSES':
    ('rest_framework.authentication.TokenAuthentication',
 )}


#     # If another provider
#     "SMS_AUTH_PROVIDER_LOGIN":"SMS provider login"
#     "SMS_AUTHPROVIDER_PASSWORD": "SMS provider password"

PASSWORDLESS_AUTH = {
   'PASSWORDLESS_AUTH_TYPES': ['MOBILE'],

}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/home/ssoad/etaka_backend/static'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# TWILIO_ACCOUNT_SID ='ACf365d18367e7db2daee18446714fc6e0'
# TWILIO_AUTH_TOKEN = '108846b736fb95458c7766498b5ff168'

PHONE_VERIFICATION = {
    "BACKEND": "phone_verify.backends.twilio.TwilioBackend",
    "OPTIONS": {
        # "SID": "ACf365d18367e7db2daee18446714fc6e0",
        # "SECRET": "108846b736fb95458c7766498b5ff168",
        "SID": "AC",
        "SECRET": "108",
        "FROM": "+14156809126",
        "SANDBOX_TOKEN": "123456",
    },
    "TOKEN_LENGTH": 6,
    "MESSAGE": "Welcome to {app}! Please use security code {security_code} to proceed.",
    "APP_NAME": "eTaka",
    "SECURITY_CODE_EXPIRATION_TIME": 3600,  # In seconds only
    "VERIFY_SECURITY_CODE_ONLY_ONCE": False,  # If False, then a security code can be used multiple times for verification
}


# DEFAULTS = {
#
#     # Allowed auth types, can be EMAIL, MOBILE, or both.
#     'PASSWORDLESS_AUTH_TYPES': ['MOBILE'],
#
#     # URL Prefix for Authentication Endpoints
#     'PASSWORDLESS_AUTH_PREFIX': 'auth/',
#
#     #  URL Prefix for Verification Endpoints
#     'PASSWORDLESS_VERIFY_PREFIX': 'auth/verify/',
#
#     # Amount of time that tokens last, in seconds
#     'PASSWORDLESS_TOKEN_EXPIRE_TIME': 15 * 60,
#
#     # The user's email field name
#     'PASSWORDLESS_USER_EMAIL_FIELD_NAME': 'email',
#
#     # The user's mobile field name
#     'PASSWORDLESS_USER_MOBILE_FIELD_NAME': 'mobile',
#
#     # Marks itself as verified the first time a user completes auth via token.
#     # Automatically unmarks itself if email is changed.
#     'PASSWORDLESS_USER_MARK_EMAIL_VERIFIED': False,
#     'PASSWORDLESS_USER_EMAIL_VERIFIED_FIELD_NAME': 'email_verified',
#
#     # Marks itself as verified the first time a user completes auth via token.
#     # Automatically unmarks itself if mobile number is changed.
#     'PASSWORDLESS_USER_MARK_MOBILE_VERIFIED': False,
#     'PASSWORDLESS_USER_MOBILE_VERIFIED_FIELD_NAME': 'mobile_verified',
#
#     # The email the callback token is sent from
#     'PASSWORDLESS_EMAIL_NOREPLY_ADDRESS': None,
#
#     # The email subject
#     'PASSWORDLESS_EMAIL_SUBJECT': "Your Login Token",
#
#     # A plaintext email message overridden by the html message. Takes one string.
#     'PASSWORDLESS_EMAIL_PLAINTEXT_MESSAGE': "Enter this token to sign in: %s",
#
#     # The email template name.
#     'PASSWORDLESS_EMAIL_TOKEN_HTML_TEMPLATE_NAME': "passwordless_default_token_email.html",
#
#     # Your twilio number that sends the callback tokens.
#     'PASSWORDLESS_MOBILE_NOREPLY_NUMBER': '+14156809126',
#
#     # The message sent to mobile users logging in. Takes one string.
#     'PASSWORDLESS_MOBILE_MESSAGE': "Use this code to log in: %s",
#
#     # Registers previously unseen aliases as new users.
#     'PASSWORDLESS_REGISTER_NEW_USERS': True,
#
#     # Suppresses actual SMS for testing
#     'PASSWORDLESS_TEST_SUPPRESSION': False,
#
#     # Context Processors for Email Template
#     'PASSWORDLESS_CONTEXT_PROCESSORS': [],
#
#     # The verification email subject
#     'PASSWORDLESS_EMAIL_VERIFICATION_SUBJECT': "Your Verification Token",
#
#     # A plaintext verification email message overridden by the html message. Takes one string.
#     'PASSWORDLESS_EMAIL_VERIFICATION_PLAINTEXT_MESSAGE': "Enter this verification code: %s",
#
#     # The verification email template name.
#     'PASSWORDLESS_EMAIL_VERIFICATION_TOKEN_HTML_TEMPLATE_NAME': "passwordless_default_verification_token_email.html",
#
#     # The message sent to mobile users logging in. Takes one string.
#     'PASSWORDLESS_MOBILE_VERIFICATION_MESSAGE': "Enter this verification code: %s",
#
#     # Automatically send verification email or sms when a user changes their alias.
#     'PASSWORDLESS_AUTO_SEND_VERIFICATION_TOKEN': False,
#
#     # What function is called to construct an authentication tokens when
#     # exchanging a passwordless token for a real user auth token. This function
#     # should take a user and return a tuple of two values. The first value is
#     # the token itself, the second is a boolean value representating whether
#     # the token was newly created.
#     'PASSWORDLESS_AUTH_TOKEN_CREATOR': 'drfpasswordless.utils.create_authentication_token',
#
#     # What function is called to construct a serializer for drf tokens when
#     # exchanging a passwordless token for a real user auth token.
#     'PASSWORDLESS_AUTH_TOKEN_SERIALIZER': 'drfpasswordless.serializers.TokenResponseSerializer',
#
#     # A dictionary of demo user's primary key mapped to their static pin
#     'PASSWORDLESS_DEMO_USERS': {},
#
#     'PASSWORDLESS_EMAIL_CALLBACK': 'drfpasswordless.utils.send_email_with_callback_token',
#     'PASSWORDLESS_SMS_CALLBACK': 'drfpasswordless.utils.send_sms_with_callback_token',
#
# # Token Generation Retry Count
#     'PASSWORDLESS_TOKEN_GENERATION_ATTEMPTS': 3,
#
# }