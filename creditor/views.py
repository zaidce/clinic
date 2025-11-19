from django.shortcuts import render
from rest_framework import viewsets

from  .serializer import CreditorSerializer
from .models import Creditor
class CreditorViewSet(viewsets.ModelViewSet):
    queryset = Creditor.objects.all()
    serializer_class = CreditorSerializer