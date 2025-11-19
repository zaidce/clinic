from rest_framework import serializers
from .models import     Punishment

class PunishmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Punishment
        fields='__all__'