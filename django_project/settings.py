"""
Django settings for django_project project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
import django_heroku
from pathlib import Path
from machina import MACHINA_MAIN_TEMPLATE_DIR
from machina import MACHINA_MAIN_STATIC_DIR




# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!$#0($$s(ya(@0by*)n7bnr=82rzk)dk!1nt)v@#^_dd7%_pk@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
#SITE_ID=1
TAWKTO_ID_SITE='https://tawk.to/chat/6091e39f185beb22b30a11de/1f4su2aac'
INSTALLED_APPS = [
    'orders',
    'cart',
    'especialista',
    'stripe_app',
    'django.contrib.humanize',
    'history',
    'hitcount',
    'pages_views',
    'admindashboard',
    'common',
    'Profile',
    'userprofile',
    'django_cleanup',
    #'django_project.apps.SuitConfig',
    'tawkto',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrapform',
    'bootstrap',
    
    'crispy_forms',
    'django_app',
    'blog_noticias',
    'ckeditor',
    'ckeditor_uploader',
    
    'dashboard',
    'sobre',
    
    
    
    
    

    # Machina dependencies:
    'mptt',
    'haystack',
    'widget_tweaks',
    'whoosh',

    # Machina apps:
    'machina',
    'machina.apps.forum',
    'machina.apps.forum_conversation',
    'machina.apps.forum_conversation.forum_attachments',
    'machina.apps.forum_conversation.forum_polls',
    'machina.apps.forum_feeds',
    'machina.apps.forum_moderation',
    'machina.apps.forum_search',
    'machina.apps.forum_tracking',
    'machina.apps.forum_member',
    'machina.apps.forum_permission',
]


MACHINA_FORUM_NAME = 'FÓRUM - MERLIN RESEARCH'

MACHINA_TOPIC_ANSWER_SUBJECT_PREFIX = 'Reposta'

MACHINA_FORUM_TOPICS_NUMBER_PER_PAGE = 5

MACHINA_PROFILE_RECENT_POSTS_NUMBER = 5



MACHINA_MARKUP_WIDGET = 'ckeditor.widgets.CKEditorWidget'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'machina.apps.forum_permission.middleware.ForumPermissionMiddleware',
]

ROOT_URLCONF = 'django_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        
        'DIRS': [
            MACHINA_MAIN_TEMPLATE_DIR,
            os.path.join(BASE_DIR, 'templates'),
            
            ],
        'APP_DIRS': True,
            
        
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'machina.core.context_processors.metadata',
                
                

            ],

            
        },
    },
]

WSGI_APPLICATION = 'django_project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'


#STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

CKEDITOR_BASE_PATH = '/static/ckeditor/ckeditor'
CKEDITOR_UPLOAD_PATH = 'media/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 400,
        'width': '100%',
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    MACHINA_MAIN_STATIC_DIR,
    os.path.join(BASE_DIR, "django_project/static/")
]

STATIC_ROOT = '~/Documentos/Programming Store/Clientes/Alessandro Manaus/Merlin Research/projeto em si$ ing Store/Clientes/Alessandro Manaus/static'



CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'machina_attachments': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp',
    },
}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}

SITE_ID=1

LOGIN_REDIRECT_URL = 'dashboard'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


django_heroku.settings(locals())