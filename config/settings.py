
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u$#upa)*hm6um^sd$l6qu%gl5lkm9t1jwcgogo&(k_f=o07w$l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.users',
    'apps.brevets',
    'apps.documents',
    'apps.paiements',
    'apps.recours',
    'apps.notifications',
    'rest_framework',

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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'gestion_brevets_db', # Le nom que vous venez de créer
        'USER': 'postgres',           # Utilisateur par défaut de Postgres
        'PASSWORD': 'abdou1234', # Celui choisi à l'installation de Postgres
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'

import os

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# config/settings.py
AUTH_USER_MODEL = 'users.Utilisateur'

# ==========================
# Jazzmin Settings – Full Dark Mode + Icons
# ==========================

JAZZMIN_SETTINGS = {
    # ─── Informations générales ───
    "site_title": "Gestion Brevets",
    "site_header": "Gestion Brevets",
    "site_brand": "Gestion Brevets",
    "site_logo": "images/logo-sonatrach.jpg",
    
    # ─── Thème & UI ───
    "theme": "darkly",                  # Dark mode complet
    "default_theme_mode": "dark",       # ⚡ Remplace dark_mode_theme déprécié
    "show_ui_builder": False,           # Empêche modification UI via le builder
    
    # ─── Sidebar ───
    "navigation_expanded": True,
    "order_with_respect_to": [
        "dashboard",
        "brevets",
        "inventeurs",
        "deposants",
        "documents",
        "paiements",
        "recours",
        "notifications",
        "users",
        "auth",
    ],
    
    # ─── Icons par app / modèle ───
    "icons": {
        # Users / Auth
        "auth": "fas fa-users-cog",
        "users.Utilisateur": "fas fa-user",
        "users.Role": "fas fa-user-tag",
        
        # Brevets
        "brevets": "fas fa-folder",
        "brevets.Brevet": "fas fa-lightbulb",
        "brevets.DemandeBrevet": "fas fa-file-alt",
        
        # Inventeurs & Déposants
        "inventeurs.Inventeur": "fas fa-user-astronaut",
        "deposants.Deposant": "fas fa-user-tie",
        
        # Documents
        "documents": "fas fa-folder-open",
        "documents.Document": "fas fa-file",
        "documents.TypeDocument": "fas fa-file-medical",
        
        # Paiements
        "paiements": "fas fa-credit-card",
        "paiements.Paiement": "fas fa-money-bill-wave",
        
        # Notifications
        "notifications": "fas fa-bell",
        "notifications.Notification": "fas fa-bell",
        
        # Recours
        "recours": "fas fa-balance-scale",
        "recours.Recours": "fas fa-gavel",
        
        # Dashboard
        "dashboard": "fas fa-chart-line",
    }
}

# ─── UI Tweaks supplémentaires ───
JAZZMIN_UI_TWEAKS = {
    # Navbar
    "navbar": "navbar-dark",
    "brand_colour": "navbar-primary",
    
    # Accent color général
    "accent": "accent-info",
    
    # Sidebar
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    
    # Full dark mode bootstrap
    "dark_mode_theme": "darkly",        # 🔹 support backward compatibility
}