from django.contrib import admin
from import_export.admin import ExportMixin
from .models import Timesheet

class TimesheetAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ("job", "user", "start_time", "end_time", "hours")

admin.site.register(Timesheet, TimesheetAdmin)
