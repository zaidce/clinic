from django.shortcuts import render
from rest_framework import viewsets

from  .serializer import DruginSerializer
from .models import Drugin
class DruginViewSet(viewsets.ModelViewSet):
    queryset = Drugin.objects.all()
    serializer_class = DruginSerializer