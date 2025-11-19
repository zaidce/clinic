from django.shortcuts import render
from rest_framework import viewsets

from  .serializer import OutcomeSerializer
from .models import Outcome
class OutcomeViewSet(viewsets.ModelViewSet):
    queryset = Outcome.objects.all()
    serializer_class = OutcomeSerializer