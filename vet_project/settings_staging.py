from vet_project.settings import *

DEBUG = False
ALLOWED_HOSTS = ['52.14.56.255', 'vet.toubhans.org']

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
