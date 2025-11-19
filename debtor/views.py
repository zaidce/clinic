from django.shortcuts import render
from rest_framework import viewsets

from  .serializer import DebtorSerializer
from .models import Debtor
class DebtorViewSet(viewsets.ModelViewSet):
    queryset = Debtor.objects.all()
    serializer_class = DebtorSerializer