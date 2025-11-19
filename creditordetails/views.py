from django.shortcuts import render
from rest_framework import viewsets

from  .serializer import CreditorDetailsSerializer
from .models import CreditorDetails
class CreditorDetailsViewSet(viewsets.ModelViewSet):
    queryset = CreditorDetails.objects.all()
    serializer_class = CreditorDetailsSerializer