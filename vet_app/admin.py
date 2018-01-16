from django.contrib import admin
from .models import People
from .models import PeopleAdmin
from .models import Service


admin.site.register(People, PeopleAdmin)
admin.site.register(Service)
