from .base import *

#############################
#      PROD Settings
#############################

ALLOWED_HOSTS = [".herokuapp.com", ".kinnectcareers.com"]

ADMINS = MANAGERS = [
    {"Rick Nunes", "sanunes.ricardo@gmail.com"},
    {"Thanisha Pariage", "tp1590@nyu.edu"},
]

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

############################
#    Security Settings
############################

CSRF_COOKIE_HTTPONLY = True
CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_NAME = "kinnectcareers_sessionid"
SESSION_COOKIE_SECURE = True
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

X_FRAME_OPTIONS = "DENY"

REST_FRAMEWORK = {
    "DEFAUL_PERMISSION_CLASSES": {
        "rest_framework.permissions.IsAuthenticatedOrReadOnly",
    }
}

