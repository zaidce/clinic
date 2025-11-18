from django.db import models
from datetime import datetime
# Create your models here.
class Drug(models.Model):
    name=models.CharField(max_length=200)
    dose=models.CharField(max_length=200,blank=True,null=True)
    days=models.IntegerField(default=0)
    times=models.IntegerField(default=0)
    note=models.CharField(max_length=200,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)