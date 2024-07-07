from .settings import *

DEBUG = False 

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['daveprocode.com', 'www.daveprocode.com']

DATABASES = {
    'default': dj_database_url.config()
}

django_heroku.settings(locals())
