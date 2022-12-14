import os

from dotenv import load_dotenv

# Load .env
load_dotenv()

# Set the project base directory
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

DEBUG = os.environ.get("DEBUG", False)

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-fjwo(3n$w7oo_38y_r_txb3c7&p$9hlq=ra0hp154!j+arkwki",
)

ALLOWED_HOSTS = os.environ.get(
    "DJANGO_ALLOWED_HOSTS",
    "*",
).split(", ")

INTERNAL_IPS = os.environ.get(
    "DJANGO_INTERNAL_IPS",
    "127.0.0.1",
)

RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition
INSTALLED_APPS = [
    "artifica.home",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sitemaps",
    "django_browser_reload",
    "debug_toolbar",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "modelcluster",
    "taggit",
    "wagtail.admin",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.documents",
    "wagtail.embeds",
    "wagtail.images",
    "wagtail.search",
    "wagtail.sites",
    "wagtail.snippets",
    "wagtail.users",
    "wagtail",
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.cache.FetchFromCacheMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "artifica.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            "artifica/templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "artifica.wsgi.application"


# Database
DATABASES = {
    "default": {
        "ENGINE": os.environ.get("DATABASE_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get(
            "DATABASE_NAME", os.path.join(PROJECT_DIR, "db.sqlite3")
        ),
        "USER": os.environ.get("DATABASE_USER", "admin"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD", "password"),
        "HOST": os.environ.get("DATABASE_HOST", "localhost"),
        "PORT": os.environ.get("DATABASE_PORT", "5432"),
    }
}


# Cache
CACHES = {
    "default": {
        "BACKEND": os.environ.get(
            "CACHE_ENGINE",
            "django.core.cache.backends.dummy.DummyCache",
        ),
        "LOCATION": os.environ.get(
            "CACHE_URL",
            "cache",
        ),
    },
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [
    os.path.join(PROJECT_DIR, "artifica/static"),
    os.path.join(PROJECT_DIR, "artifica/frontend/build"),
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# ManifestStaticFilesStorage is recommended in production, to prevent outdated
# JavaScript / CSS assets being served from cache.
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
STATIC_ROOT = os.path.join(PROJECT_DIR, "staticfiles")
STATIC_URL = "/static/"

MEDIA_ROOT = os.path.join(PROJECT_DIR, "media")
MEDIA_URL = "/media/"


# Wagtail settings
WAGTAIL_SITE_NAME = "artifica"

# Search
WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
WAGTAILADMIN_BASE_URL = "http://example.com"

# Logging
LOGGING_FORMATTERS = {
    "simple": {
        "format": "{levelname} {message}",
        "style": "{",
    },
    "verbose": {
        "format": "{name} {levelname} {asctime} {module} {process:d} {thread:d} {message}",
        "style": "{",
    },
}

LOGGING_HANDLERS = {
    "console": {
        "class": "logging.StreamHandler",
        "formatter": "simple",
    },
    "basic_file": {
        "class": "logging.FileHandler",
        "filename": os.getenv("DJANGO_LOG_BASIC_FILE", f"{PROJECT_DIR}/logs/basic.log"),
        "mode": "a",
        "encoding": "utf-8",
        "formatter": "simple",
    },
    "detailed_file": {
        "class": "logging.FileHandler",
        "filename": os.getenv(
            "DJANGO_LOG_DETAILED_FILE", f"{PROJECT_DIR}/logs/detailed.log"
        ),
        "mode": "a",
        "encoding": "utf-8",
        "formatter": "verbose",
    },
}

LOGGING_LOGGERS = {
    "django": {
        "handlers": ["console", "basic_file"],
        "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
        "propagate": False,
    },
    "django-request": {
        "django-request": {
            "handlers": ["detailed_file"],
            "level": "WARNING",
            "propagate": False,
        }
    },
    "django.db.backends": {
        "handlers": ["console", "detailed_file"],
        "level": "ERROR",
        "propagate": False,
    },
}

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": LOGGING_FORMATTERS,
    "handlers": LOGGING_HANDLERS,
    "loggers": LOGGING_LOGGERS,
}

# CSRF tokens
CSRF_TRUSTED_ORIGINS = os.environ.get(
    "DJANGO_CSRF_TRUSTED_ORIGINS",
    "http://localhost",
).split(", ")
