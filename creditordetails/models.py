from django.db import models
from datetime import datetime

from creditor.models import Creditor
# Create your models here.
class CreditorDetails(models.Model):
    creditor_id=models.ForeignKey(Creditor,related_name="CreditorDetails",on_delete=models.CASCADE,verbose_name="الدائن")
    amount=models.IntegerField(verbose_name="المبلغ")
    note=models.CharField(max_length=200,blank=True,null=True,verbose_name="الملاحظات")
    creditorDetailsDate=models.DateField(default=datetime.now,verbose_name="التاريخ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.amount)+"  "+str(self.creditorDetailsDate)
    class Meta:
        verbose_name = "تسديد"  # Singular name
        verbose_name_plural = "تسديد الدائنين" # Plural name
        #,verbose_name="القسم"