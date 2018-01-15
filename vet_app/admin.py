from django.contrib import admin
from .models import People
from .models import PeopleAdmin


admin.site.register(People, PeopleAdmin)
