from rest_framework import serializers
from .models import     Drugout

class DrugoutSerializer(serializers.ModelSerializer):
    class Meta:
        model=Drugout
        fields='__all__'