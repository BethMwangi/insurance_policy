from rest_framework import serializers
from field_history.models import FieldHistory

from .models import Policy, Quote
from accounts.serializers import UserSerializer


class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = ['name', 'slug' , 'status']


class HistoricalRecordsSerializer(serializers.ListField):
    child = serializers.DictField()

    def to_representation(self, data):
        return super().to_representation(data.values())


class QuoteSerializer(serializers.ModelSerializer):
    age = serializers.CharField(source='get_user_age', read_only=True)
    quote_price = serializers.CharField(source='quoted_price', read_only=True)
    status = serializers.SerializerMethodField()
    history = HistoricalRecordsSerializer(read_only=True)
    customer = UserSerializer()

    class Meta:
        depth = 1
        model = Quote
        fields = '__all__'
        read_only_fields = ['premium']


    def get_status(self, obj):
        return obj.get_status_display()


   

 
 