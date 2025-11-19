from rest_framework import serializers
from .models import     SessionDrug

class SessionDrugSerializer(serializers.ModelSerializer):
    class Meta:
        model=SessionDrug
        fields='__all__'