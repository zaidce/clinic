from django.shortcuts import render
from rest_framework import viewsets

from  .serializer import StaffSerializer
from .models import Staff
class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer