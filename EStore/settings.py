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
    # Browser tab title & header
    "site_title": "Vogue Store Admin",
    "site_header": "VOGUE STORE",
    "site_brand": "👗 Vogue Store",

    # Top nav welcome text
    "welcome_sign": "Welcome to Vogue Store Admin Panel",
    "copyright": "Vogue Store © 2025",

    # Search bar in top nav — searches across these models
    "search_model": ["store.Product", "store.Order", "auth.User"],

    # User avatar
    "user_avatar": None,

    # Top nav links (quick access)
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "🏠 View Site", "url": "/", "new_window": True},
        {"model": "store.Product"},
        {"model": "store.Order"},
    ],

    # Sidebar links per model
    "usermenu_links": [
        {"name": "🏠 View Site", "url": "/", "new_window": True},
    ],

    "show_sidebar": True,
    "navigation_expanded": True,

    # Hide these apps from the sidebar
    "hide_apps": [],
    "hide_models": [],

    # Custom icons for models (Font Awesome 5)
    "icons": {
        "auth":                  "fas fa-users-cog",
        "auth.user":             "fas fa-user",
        "auth.Group":            "fas fa-users",
        "store.Product":         "fas fa-tshirt",
        "store.Order":           "fas fa-shopping-bag",
        "store.Cart":            "fas fa-shopping-cart",
        "store.Wishlist":        "fas fa-heart",
        "store.Contact":         "fas fa-envelope",
        "store.Rating":          "fas fa-star",
    },
    "default_icon_parents": "fas fa-folder",
    "default_icon_children": "fas fa-circle",

    # Render out the change list filters in a modal
    "related_modal_active": True,

    # Custom CSS / JS loaded only in admin (won't affect main site)
    "custom_css": "css/admin_custom.css",
    "custom_js": None,

    # Whether to show the UI customizer button
    "show_ui_builder": False,

    # Order sidebar items
    "order_with_respect_to": [
        "store",
        "store.Product",
        "store.Order",
        "store.Cart",
        "store.Wishlist",
        "store.Contact",
        "store.Rating",
        "auth",
    ],
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": False,
    "brand_small_text": False,

    # Top navbar colour
    "brand_colour": False,
    "accent": "accent-pink",

    # navbar: navbar-white, navbar-dark, navbar-primary, etc.
    "navbar": "navbar-dark",
    "no_navbar_border": True,

    # Sidebar style
    "sidebar": "sidebar-dark-pink",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": True,
    "sidebar_nav_compact_style": False,
    "sidebar_nav_flat_style": False,
    "sidebar_nav_legacy_style": False,

    # Bootswatch theme
    "theme": "flatly",
    "dark_mode_theme": "darkly",

    # Button styles
    "button_classes": {
        "primary":   "btn-primary",
        "secondary": "btn-secondary",
        "info":      "btn-info",
        "warning":   "btn-warning",
        "danger":    "btn-danger",
        "success":   "btn-success",
    },

    # Change view action buttons
    "actions_sticky_top": True,
}
# ──────────────────────────────────────────────────────────────────────────────

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
