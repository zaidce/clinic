from rest_framework import serializers
from .models import     Sessionx

class SessionxSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sessionx
        fields='__all__'