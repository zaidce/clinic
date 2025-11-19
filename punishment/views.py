from django.shortcuts import render
from rest_framework import viewsets

from  .serializer import PunishmentSerializer
from .models import Punishment
class PunishmentViewSet(viewsets.ModelViewSet):
    queryset = Punishment.objects.all()
    serializer_class = PunishmentSerializer