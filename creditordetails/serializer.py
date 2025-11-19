from rest_framework import serializers
from .models import     CreditorDetails

class CreditorDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=CreditorDetails
        fields='__all__'