from rest_framework import serializers
from .models import     ReadyPrescription

class ReadyPrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReadyPrescription
        fields='__all__'