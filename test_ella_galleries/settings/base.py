from os.path import dirname, join, normpath, pardir

FILE_ROOT = normpath(join(dirname(__file__), pardir))

USE_I18N = True
USE_TZ = True

MEDIA_ROOT = join(FILE_ROOT, 'static')


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'test_ella_galleries.template_loader.GlobalMemTemplateLoader',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
)

ROOT_URLCONF = 'test_ella_galleries.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    join(FILE_ROOT, 'templates'),

)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.media',
    'django.contrib.auth.context_processors.auth',
)

TEMPLATE_OPTIONS = {
    'context_processors': TEMPLATE_CONTEXT_PROCESSORS,
    'loaders': TEMPLATE_LOADERS,
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'APP_DIRS': True,
        # 'DIRS': TEMPLATE_DIRS,
        'OPTIONS': TEMPLATE_OPTIONS
    },
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.redirects',
    'django.contrib.admin',

    'ella.core',
    'ella.photos',
    'ella.articles',
    'ella_galleries',
)

TEST_RUNNER = 'django.test.runner.DiscoverRunner'
