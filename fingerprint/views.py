from django.shortcuts import render
from rest_framework import viewsets

from  .serializer import FingerPrintMdlSerializer
from .models import FingerPrintMdl
class FingerPrintMdlViewSet(viewsets.ModelViewSet):
    queryset = FingerPrintMdl.objects.all()
    serializer_class = FingerPrintMdlSerializer