from django.db import models
from datetime import datetime

from staff.models import Staff
# Create your models here.
class Punishment(models.Model):
    staff_id=models.ForeignKey(Staff,related_name="PunishmentStaff",on_delete=models.CASCADE,verbose_name="الموظف")
    cost=models.IntegerField(default=0,verbose_name="الخصم")
    reasone=models.CharField(max_length=200,verbose_name="السبب" )
    isDone=models.BooleanField(default=False,verbose_name="تم التنفيذ")
    punishmentDate=models.DateField(default=datetime.now,verbose_name="التاريخ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.staff_id.name
    class Meta:
        verbose_name = "عقوبة"  # Singular name
        verbose_name_plural = "العقوبات" # Plural name
        #,verbose_name="القسم"