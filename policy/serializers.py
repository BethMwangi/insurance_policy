from rest_framework import serializers
from simple_history.models import HistoricalRecords

from .models import Policy

class HistoricalRecordsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalRecords
        fields = '__all__'

class PolicySerializer(serializers.ModelSerializer):
    histories = HistoricalRecordsSerializer(many=True, read_only=True)

    class Meta:
        model = Policy
        fields = ['name', 'slug' , 'status', 'histories']
