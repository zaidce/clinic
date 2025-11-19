from django.shortcuts import render
from rest_framework import viewsets

from  .serializer import OfferSerializer
from .models import Offer
class OfferViewSet(viewsets.ModelViewSet):
    queryset = Offer.objects.all()
    serializer_class = OfferSerializer