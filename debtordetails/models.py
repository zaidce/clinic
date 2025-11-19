from django.db import models
from datetime import datetime

from debtor.models import Debtor
# Create your models here.
class DebtorDetail(models.Model):
    debtor_id=models.ForeignKey(Debtor,related_name="DebtorDetails",on_delete=models.CASCADE,verbose_name="المدين")
    amount=models.IntegerField(verbose_name="المبلغ")
    note=models.CharField(max_length=200,blank=True,null=True,verbose_name="الملاحظات")
    debtorDetailDate=models.DateField(default=datetime.now,verbose_name="التاريخ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.amount)+"  "+str(self.debtorDetailDate)
    class Meta:
        verbose_name = "تسديد"  # Singular name
        verbose_name_plural = "تسديد المدينين" # Plural name
        #,verbose_name="القسم"