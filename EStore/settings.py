
from pathlib import Path
import os
from decouple import config


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)

ALLOWED_HOSTS = ['*']

JAZZMIN_SETTINGS = {
    # ── Branding ──
    "site_title": "Vogue Store",
    "site_header": "Vogue Store",
    "site_brand": "VOGUE",
    "welcome_sign": "Welcome to Vogue Store Admin",


    # ── Icons ──
    "site_icon": None,  # add your logo path if you have one

    # ── Top Menu ──
    "topmenu_links": [
        {"name": " Home", "url": "admin:index"},
        {"name": " Visit Store", "url": "/", "new_window": True},
    ],

    # ── Sidebar Icons (per model) ──
    "icons": {
        "auth":                     "fas fa-users-cog",
        "auth.user":                "fas fa-user",
        "auth.group":               "fas fa-users",
        "store.orders":             "fas fa-shopping-bag",
        "store.products":           "fas fa-tshirt",
        "store.carts":              "fas fa-shopping-cart",
        "store.contacts":           "fas fa-envelope",
        "store.ratings":            "fas fa-star",
        "store.wishlists":          "fas fa-heart",
    },
    "default_icon_parents":  "fas fa-store",
    "default_icon_children": "fas fa-circle-dot",

    # ── UI Tweaks ──
    "show_sidebar":             True,
    "navigation_expanded":      True,
    "hide_apps":                [],
    "hide_models":              [],
    "related_modal_active":     True,   
    "custom_links":             {},
    "show_ui_builder":          True,   
}


JAZZMIN_UI_TWEAKS = {
    "theme":                     "flatly",              
    "dark_mode_theme":           None,                  

    "navbar":                    "navbar-white navbar-light",  
    "no_navbar_border":          False,
    "navbar_fixed":              True,
    "brand_colour":              "navbar-light",

    "sidebar":                   "sidebar-light-indigo", 
    "sidebar_fixed":             True,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_child_indent":  True,

    "accent":                    "accent-indigo",

    "layout_boxed":              False,
    "footer_fixed":              False,
    "actions_sticky_top":        True,
}       
# ─── Jazzmin Admin Theme ───────────────────────────────────────────────────────

JAZZMIN_SETTINGS = {
    "site_title": "Vogue Store Admin",
    "site_header": "VOGUE STORE",
    "site_brand": "Vogue Store",
    "welcome_sign": "Welcome to Vogue Store Admin Panel",
    "copyright": "Vogue Store © 2025",
    "search_model": ["store.Product", "store.Order", "auth.User"],
    "user_avatar": None,
    "topmenu_links": [
        {"name": "Home", "url": "admin:index"},
        {"name": "View Site", "url": "/", "new_window": True},
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "icons": {
        "auth":          "fas fa-users-cog",
        "auth.user":     "fas fa-user",
        "auth.Group":    "fas fa-users",
        "store.Product": "fas fa-tshirt",
        "store.Order":   "fas fa-shopping-bag",
        "store.Cart":    "fas fa-shopping-cart",
        "store.Wishlist":"fas fa-heart",
        "store.Contact": "fas fa-envelope",
        "store.Rating":  "fas fa-star",
    },
    "default_icon_parents": "fas fa-folder",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": True,
    "show_ui_builder": False,
}


JAZZMIN_UI_TWEAKS = {
    "accent": "accent-pink",
    "navbar": "navbar-dark",
    "no_navbar_border": True,
    "sidebar": "sidebar-dark-pink",
    "sidebar_nav_child_indent": True,
    "theme": "flatly",
    "dark_mode_theme": "darkly",
    "actions_sticky_top": True,
}


INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store',
    'jazzmin',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'EStore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'EStore.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Email — fill in your credentials in a .env file, not here
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
