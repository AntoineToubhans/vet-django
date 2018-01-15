from vet_project.settings import *

DEBUG = False
ALLOWED_HOSTS = ['52.14.42.220', 'vet.toubhans.org']

DATABASES = {
 'default': {
     'ENGINE': 'django.db.backends.postgresql',
     'NAME': 'postgres',
     'USER': 'postgres',
     'PASSWORD': 'postgres',
     'HOST': 'localhost',
     'PORT': 5432,
 }
}
