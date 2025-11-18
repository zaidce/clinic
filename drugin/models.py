from django.db import models
from datetime import datetime

from staff.models import Staff
# Create your models here.
class Drugin(models.Model):
    staff_id=models.ForeignKey(Staff,related_name="Staff",on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=200)
    unit=models.IntegerField(default=0)
    quantity=models.IntegerField(default=0)
    buyPrice=models.IntegerField(default=0)
    sellPrice=models.IntegerField(default=0)
    minLevel=models.IntegerField(default=0)
    entryDate=models.DateTimeField(default=datetime.now)
    expireDate=models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name