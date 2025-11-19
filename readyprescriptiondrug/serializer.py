from rest_framework import serializers
from .models import     ReadyPrescriptionDrug

class ReadyPrescriptionDrugSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReadyPrescriptionDrug
        fields='__all__'