from django.contrib import admin
from django.contrib.admin.models import LogEntry
from solo.admin import SingletonModelAdmin

from .models import ClinicConfiguration
from .models import People
from .models import PeopleAdmin
from .models import Service
from .models import ServiceAdmin
from .models import LogEntryAdmin


admin.site.register(ClinicConfiguration, SingletonModelAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(LogEntry, LogEntryAdmin)
