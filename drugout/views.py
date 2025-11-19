from django.shortcuts import render
from rest_framework import viewsets

from  .serializer import DrugoutSerializer
from .models import Drugout
class DrugoutViewSet(viewsets.ModelViewSet):
    queryset = Drugout.objects.all()
    serializer_class = DrugoutSerializer