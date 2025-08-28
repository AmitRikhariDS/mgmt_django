from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["title", "client", "description", "assigned_engineer", "status", "due_date"]
