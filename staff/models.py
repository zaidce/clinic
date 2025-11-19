from django.db import models
from datetime import datetime
# Create your models here.
class Staff(models.Model):
    name=models.CharField(max_length=200,blank=True,null=True)
    job=models.CharField(max_length=200,blank=True,null=True)
    address=models.CharField(max_length=200,blank=True,null=True)
    phone=models.CharField(max_length=200,blank=True,null=True)
    specialize=models.CharField(max_length=200,blank=True,null=True)
    salary=models.IntegerField(default=0)
    isBanned=models.BooleanField(default=False)
    isAdmin=models.BooleanField(default=False)
    username=models.CharField(max_length=200,blank=True,null=True)
    password=models.CharField(max_length=200,blank=True,null=True)
    totalPercent=models.IntegerField(default=0)
    nextPercent=models.IntegerField(default=0)
    amountThreshold=models.IntegerField(default=0)
    startDate=models.DateField(default=datetime.now)
    endDate=models.DateField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name