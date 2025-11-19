from django.shortcuts import render
from rest_framework import viewsets

from  .serializer import MistakeSerializer
from .models import Mistake
class MistakeViewSet(viewsets.ModelViewSet):
    queryset = Mistake.objects.all()
    serializer_class = MistakeSerializer