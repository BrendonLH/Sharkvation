from dataclasses import fields
from statistics import mode
from rest_framework import serializers
from .models import Shark

class SharkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shark
        fields = ("id","name","description", "location", "avg_length", "diet")