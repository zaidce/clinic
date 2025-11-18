from django.db import models
from datetime import datetime

from client.models import Client
# Create your models here.
class Creditor(models.Model):
    client_id=models.ForeignKey(Client,related_name="Creditor",on_delete=models.CASCADE,blank=True,null=True)
    note=models.CharField(max_length=200,blank=True,null=True)
    total=models.IntegerField(default=0)
    creditorDate=models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.client_id.name