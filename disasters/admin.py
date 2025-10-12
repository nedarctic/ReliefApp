from django.contrib import admin
from .models import Disaster, SafeZone, Update

admin.site.register(Disaster)
admin.site.register(SafeZone)
admin.site.register(Update)
