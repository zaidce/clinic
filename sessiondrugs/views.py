from django.shortcuts import render
from rest_framework import viewsets

from  .serializer import SessionDrugSerializer
from .models import SessionDrug
class SessionDrugViewSet(viewsets.ModelViewSet):
    queryset = SessionDrug.objects.all()
    serializer_class = SessionDrugSerializer