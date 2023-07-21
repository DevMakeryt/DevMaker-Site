from decouple import config

from mysite.settings import BASE_DIR

# DataBase

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Send Email

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Storage

# Configuração para arquivos estáticos
STATIC_URL = f'/static/'
MEDIA_URL = f'/media/'
