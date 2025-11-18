from django.db import models
from datetime import datetime

from creditor.models import Creditor
# Create your models here.
class CreditorDetails(models.Model):
    creditor_id=models.ForeignKey(Creditor,related_name="CreditorDetails",on_delete=models.CASCADE)
    amount=models.IntegerField(default=0)
    note=models.CharField(max_length=200,blank=True,null=True)
    creditorDetailsDate=models.DateField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.amount)+"  "+str(self.creditorDetailsDate)