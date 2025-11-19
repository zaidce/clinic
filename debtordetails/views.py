from django.shortcuts import render
from rest_framework import viewsets

from  .serializer import DebtorDetailSerializer
from .models import DebtorDetail
class DebtorDetailViewSet(viewsets.ModelViewSet):
    queryset = DebtorDetail.objects.all()
    serializer_class = DebtorDetailSerializer