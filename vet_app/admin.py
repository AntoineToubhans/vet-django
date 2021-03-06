from django.contrib import admin
from django.contrib.admin.models import LogEntry

from .models import ClinicConfiguration
from .models import ClinicConfigurationAdmin
from .models import ClinicOpeningHour
from .models import News
from .models import NewsAdmin
from .models import People
from .models import PeopleAdmin
from .models import Service
from .models import ServiceAdmin
from .models import LogEntryAdmin
from .models import GalleryImage
from .models import GalleryImageAdmin


admin.site.register(ClinicConfiguration, ClinicConfigurationAdmin)
admin.site.register(ClinicOpeningHour)
admin.site.register(News, NewsAdmin)
admin.site.register(People, PeopleAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(LogEntry, LogEntryAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
