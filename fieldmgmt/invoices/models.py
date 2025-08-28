import uuid
from django.db import models
from jobs.models import Job

class Invoice(models.Model):
    STATUS_CHOICES = [
        ("draft", "Draft"),
        ("sent", "Sent"),
        ("paid", "Paid"),
    ]

    invoice_number = models.CharField(max_length=50, default=uuid.uuid4, unique=True)
    job = models.OneToOneField(Job, on_delete=models.CASCADE, related_name="invoice")
    client = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")

    def __str__(self):
        return self.invoice_number
