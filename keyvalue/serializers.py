from rest_framework import serializers, response
from django.utils import timezone
from .models import KeyValue
import datetime


class KeyValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = KeyValue
        fields = '__all__'
        
