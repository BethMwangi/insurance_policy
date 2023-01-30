from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        read_only_fields = ['age']
        exclude = ('password',)
