from django.shortcuts import render
from rest_framework import viewsets

from  .serializer import RewardSerializer
from .models import Reward
class RewardViewSet(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer