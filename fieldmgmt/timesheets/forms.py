from django import forms
from .models import Timesheet

class TimesheetForm(forms.ModelForm):
    class Meta:
        model = Timesheet
        fields = ["job", "start_time", "end_time", "hourly_rate", "notes"]
