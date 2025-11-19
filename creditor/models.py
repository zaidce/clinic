from django.db import models
from datetime import datetime

from client.models import Client
# Create your models here.
class Creditor(models.Model):
    client_id=models.ForeignKey(Client,related_name="Creditor",on_delete=models.CASCADE,verbose_name="الدائن")
    note=models.CharField(max_length=200,blank=True,null=True,verbose_name="الملاحظات")
    total=models.IntegerField(verbose_name="المبلغ")
    creditorDate=models.DateField(default=datetime.now,verbose_name="التاريخ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.client_id.name
    class Meta:
        verbose_name = "دائن"  # Singular name
        verbose_name_plural = "الدائنين" # Plural name
        #,verbose_name="القسم"