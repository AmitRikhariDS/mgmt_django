from django.db import models
from django.conf import settings
from jobs.models import Job

class Timesheet(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="timesheets")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    hours = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.start_time and self.end_time:
            duration = (self.end_time - self.start_time).total_seconds() / 3600
            self.hours = round(duration, 2)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} - {self.job}"
