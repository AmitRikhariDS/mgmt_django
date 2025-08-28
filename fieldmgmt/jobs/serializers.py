from rest_framework import serializers
from .models import Job, JobCheckin

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"

class JobCheckinSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCheckin
        fields = "__all__"
