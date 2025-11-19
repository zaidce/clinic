from django.db import models
from datetime import datetime

from drugin.models import Drugin
from sessionx.models import Sessionx
from staff.models import Staff
# Create your models here.
class Drugout(models.Model):
    drugin_id=models.ForeignKey(Drugin,related_name="DrugoutDrugin",on_delete=models.CASCADE,verbose_name="الدواء المدخل")
    staff_id=models.ForeignKey(Staff,related_name="DrugoutStaff",on_delete=models.CASCADE,verbose_name="المدخل")
    session_id=models.ForeignKey(Sessionx,related_name="DrugoutSessionx",on_delete=models.CASCADE,verbose_name="الجلسة")
    quantity=models.IntegerField(default=0,verbose_name="الكمية")
    outDate=models.DateTimeField(default=datetime.now,verbose_name="التاريخ")
    note=models.CharField(max_length=200,blank=True,null=True,verbose_name="الملاحظات")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.drugin_id.name 
    class Meta:
        verbose_name = "دواء"  # Singular name
        verbose_name_plural = "الادوية الخارجة" # Plural name
        #,verbose_name="القسم"