from django.db import models
from datetime import datetime
# Create your models here.
class Outcome(models.Model):
    outcomeDate=models.DateField(default=datetime.now)
    outcomeType=models.CharField(max_length=200)
    name=models.CharField(max_length=200)
    total=models.IntegerField(default=0)
    note=models.CharField(max_length=200,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name