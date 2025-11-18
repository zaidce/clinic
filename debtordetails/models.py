from django.db import models
from datetime import datetime

from debtor.models import Debtor
# Create your models here.
class DebtorDetail(models.Model):
    debtor_id=models.ForeignKey(Debtor,related_name="DebtorDetails",on_delete=models.CASCADE)
    amount=models.IntegerField(default=0)
    note=models.CharField(max_length=200,blank=True,null=True)
    debtorDetailDate=models.DateField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.amount)+"  "+str(self.debtorDetailDate)