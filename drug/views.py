from django.shortcuts import render
from rest_framework import viewsets

from  .serializer import DrugSerializer
from .models import Drug
class DrugViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer