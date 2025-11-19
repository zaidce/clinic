from django.shortcuts import render
from rest_framework import viewsets

from  .serializer import StaffServicPercentSerializer
from .models import StaffServicPercent
class StaffServicPercentViewSet(viewsets.ModelViewSet):
    queryset = StaffServicPercent.objects.all()
    serializer_class = StaffServicPercentSerializer