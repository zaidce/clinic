from django.shortcuts import render
from rest_framework import viewsets

from  .serializer import ReadyPrescriptionDrugSerializer
from .models import ReadyPrescriptionDrug
class ReadyPrescriptionDrugViewSet(viewsets.ModelViewSet):
    queryset = ReadyPrescriptionDrug.objects.all()
    serializer_class = ReadyPrescriptionDrugSerializer