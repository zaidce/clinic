from rest_framework import serializers
from .models import     Drugin

class DruginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Drugin
        fields='__all__'