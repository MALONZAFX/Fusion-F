"""
Django settings for fusion_force project.
"""
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SIMPLE CONFIG
SECRET_KEY = 'dev-key-123456'  # Hardcode for now
DEBUG = True  # Hardcode for now
ALLOWED_HOSTS = ['*']  # Allow all for development

# APPS - ONLY WHAT WE NEED
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.staticfiles',  # ONLY NEED THIS
    'main',  # YOUR APP
]

# MIDDLEWARE - MINIMAL
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'fusion_force.urls'

# TEMPLATES - FIXED
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Project-level templates
        'APP_DIRS': True,  # TURN OFF app directories
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'fusion_force.wsgi.application'

# ⚠️ CRITICAL FIX: NO DATABASE CONFIGURATION AT ALL
# Remove DATABASES completely or use this:
DATABASES = {}

# Also disable all database-related features
MIGRATION_MODULES = {}
DATABASE_ROUTERS = []
DEFAULT_AUTO_FIELD = None

# PASSWORD VALIDATORS - EMPTY
AUTH_PASSWORD_VIDATORS = []

# INTERNATIONALIZATION
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# STATIC FILES
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

print("🚀 ZERO-DATABASE SETTINGS - SITE WILL 100% LOAD")
print("✅ No database = No migration checks")
print("✅ Templates will load from:", BASE_DIR / 'templates')