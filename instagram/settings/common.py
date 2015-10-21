import os

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^wko(6plca@pd$9%0!e=r8aak^!a+%ul&t%*&l!o@sz*+1ox=m'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'imagekit',
    'django_jinja',
    'crispy_forms',
    'storages',
    'instagram',
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

ROOT_URLCONF = 'instagram.urls'

WSGI_APPLICATION = 'instagram.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'instagram',
        'USER': 'test',
        'PASSWORD': 'test',
        'TEST': {
            'NAME': 'instagram_test',
        }
    },
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_ROOT = os.path.join(BASE_DIR, 'static', 'dest')

TESTS_REPORTS_ROOT = os.path.join(BASE_DIR, 'reports')

AUTH_USER_MODEL = 'instagram.User'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATE_DEFAULT_NAME = 'jinja'
TEMPLATES = [
    {
        'BACKEND': 'django_jinja.backend.Jinja2',
        'NAME': 'jinja',
        'APP_DIRS': True,
        'DIRS': [],
        'OPTIONS': {
            'app_dirname': 'jinja2',
            'match_extension': '.jinja2',
            'context_processors': [
                'django.core.context_processors.csrf',
                'django.core.context_processors.debug',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.request',
                'django.contrib.messages.context_processors.messages',
                'instagram.context_processors.settings',
                'instagram.context_processors.user',
                'instagram.context_processors.webpack_dev',
            ],
            'undefined': 'jinja2.Undefined',
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.core.context_processors.csrf',
                'django.core.context_processors.debug',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.request',
                'django.contrib.auth.context_processors.auth',
            ],
        },
    },
]
CRISPY_TEMPLATE_PACK = 'bootstrap3'

DEFAULT_FILE_STORAGE = 'libs.storages.S3Storage.S3Storage'
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''