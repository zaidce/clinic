from django.shortcuts import render
from rest_framework import viewsets

from  .serializer import ReadyPrescriptionSerializer
from .models import ReadyPrescription
class ReadyPrescriptionViewSet(viewsets.ModelViewSet):
    queryset = ReadyPrescription.objects.all()
    serializer_class = ReadyPrescriptionSerializer