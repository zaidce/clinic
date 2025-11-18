from django.db import models
from datetime import datetime

from client.models import Client
# Create your models here.
class Debtor(models.Model):
    client_id=models.ForeignKey(Client,related_name="Debtor",on_delete=models.CASCADE,blank=True,null=True)
    note=models.CharField(max_length=200)
    total=models.IntegerField(default=0)
    DebtorDate=models.DateField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.client_id.name