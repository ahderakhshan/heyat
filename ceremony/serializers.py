from rest_framework import serializers
from .models import Ceremony


class CeremonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Ceremony
        fields = '__all__'
