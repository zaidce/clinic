from rest_framework import serializers
from .models import     StaffServicPercent

class StaffServicPercentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StaffServicPercent
        fields='__all__'