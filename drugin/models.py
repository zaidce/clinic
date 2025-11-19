from django.db import models
from datetime import datetime

from staff.models import Staff
# Create your models here.
class Drugin(models.Model):
    staff_id=models.ForeignKey(Staff,related_name="DruginStaff",on_delete=models.CASCADE,verbose_name="المدخل")
    name=models.CharField(max_length=200,verbose_name="الدواء")
    unit=models.CharField(max_length=200,verbose_name="الوحدة")
    quantity=models.IntegerField(verbose_name="الكمية")
    buyPrice=models.IntegerField(verbose_name="سعر الشراء")
    sellPrice=models.IntegerField(verbose_name="سعر البيع")
    minLevel=models.IntegerField(verbose_name="الحد الادنى")
    entryDate=models.DateTimeField(default=datetime.now,verbose_name="تاريخ الادخال")
    expireDate=models.DateTimeField(default=datetime.now,verbose_name="تاريخ انتهاء الصلاحية")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return  self.staffid.name+"  "+self.name
    class Meta:
        verbose_name = "دواء"  # Singular name
        verbose_name_plural = "الادوية الداخلة" # Plural name
        #,verbose_name="القسم" 