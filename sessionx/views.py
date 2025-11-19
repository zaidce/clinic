from django.shortcuts import render
from rest_framework import viewsets

from  .serializer import SessionxSerializer
from .models import Sessionx
class SessionxViewSet(viewsets.ModelViewSet):
    queryset = Sessionx.objects.all()
    serializer_class = SessionxSerializer