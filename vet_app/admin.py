from django.contrib import admin


from .models import People
from .models import PeopleAdmin
from .models import Service
from .models import ServiceAdmin


admin.site.register(People, PeopleAdmin)
admin.site.register(Service, ServiceAdmin)
