from rest_framework import serializers
from .models import     FingerPrintMdl

class FingerPrintMdlSerializer(serializers.ModelSerializer):
    class Meta:
        model=FingerPrintMdl
        fields='__all__'