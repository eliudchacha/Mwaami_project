from pathlib import Path
import os
import dj_database_url
from django.utils.translation import gettext_lazy as _

# -----------------------------
# BASE SETTINGS
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv(
    'SECRET_KEY',
    '&jn(t70lb%kryl(wkfsf)_^^2$=k7a7!4tq49nk+zlq-2!fi5x'
)

# -----------------------------
# DEBUG
# -----------------------------
DEBUG = os.getenv('DEBUG', 'False').lower() in ('False', '1')

# -----------------------------
# ALLOWED HOSTS
# -----------------------------
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'mwaami_project.onrender.com',
    'eliudwaryoba.me',
    'www.eliudwaryoba.me',
    'https://mwaami-project-1.onrender.com'
]

# CSRF settings
CSRF_COOKIE_HTTPONLY = False   # allow frontend JS to read the CSRF cookie
CSRF_TRUSTED_ORIGINS = [
    "https://mwaami-project-1.onrender.com",   # React dev server
    "http://127.0.0.1:5173",
    "https://www.eliudwaryoba.me"   # production domain
]


# Include Render external hostname if available
RENDER_HOSTNAME = os.getenv('RENDER_EXTERNAL_HOSTNAME')
if RENDER_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_HOSTNAME)

# -----------------------------
# SECURITY SETTINGS
# -----------------------------
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:5173',
    'http://127.0.0.1:5173',
    'https://mwaami_project.onrender.com',
    'https://eliudwaryoba.me',
    'https://www.eliudwaryoba.me',
    'https://mwaami-project-1.onrender.com'
]

if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# -----------------------------
# INSTALLED APPS
# -----------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party
    'rest_framework',
    'corsheaders',

    # Local apps
    'core',
]

# -----------------------------
# MIDDLEWARE
# -----------------------------
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

# -----------------------------
# CORS
# -----------------------------
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'http://127.0.0.1:5173',
    'https://mwaami_project.onrender.com',
    'https://eliudwaryoba.me',
    'https://www.eliudwaryoba.me',
    'https://mwaami-project-1.onrender.com'
]

# -----------------------------
# URLS
# -----------------------------
ROOT_URLCONF = 'config.urls'

# -----------------------------
# TEMPLATES
# -----------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# -----------------------------
# WSGI
# -----------------------------
WSGI_APPLICATION = 'config.wsgi.application'

# -----------------------------
# DATABASE
# -----------------------------
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}"
    )
}

# -----------------------------
# AUTH
# -----------------------------
AUTH_PASSWORD_VALIDATORS = []

# -----------------------------
# INTERNATIONALIZATION
# -----------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Dar_es_Salaam'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('en', _('English')),
    ('sw', _('Swahili')),
    ('fr', _('French')),
]

# -----------------------------
# STATIC & MEDIA FILES
# -----------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
] if os.path.exists(os.path.join(BASE_DIR, 'static')) else []
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'  # URL prefix
MEDIA_ROOT = os.path.join('/mnt/data', 'media')  # Path on Render persistent disk


# -----------------------------
# REST FRAMEWORK SETTINGS
# -----------------------------
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
}

# -----------------------------
# DEFAULT AUTO FIELD
# -----------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -----------------------------
# LOGGING
# -----------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING' if not DEBUG else 'INFO',
    },
}
