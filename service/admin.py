from django.contrib import admin

from .models import Taxi, StatusType, StatusDriver


admin.site.register(Taxi)
admin.site.register(StatusType)
admin.site.register(StatusDriver)