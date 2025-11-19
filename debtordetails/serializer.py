from rest_framework import serializers
from .models import     DebtorDetail

class DebtorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=DebtorDetail
        fields='__all__'