from django.db import models

from service.models import Service
from staff.models import Staff
class StaffServicPercent(models.Model):
    staff_id=models.ForeignKey(Staff,related_name="StaffServicPercentStaff",on_delete=models.CASCADE ,verbose_name="الموظف")
    service_id=models.ForeignKey(Service,related_name="StaffServicPercentService",on_delete=models.CASCADE ,verbose_name="الخدمة")
    percent=models.IntegerField(default=0,verbose_name="نسبة الموظف من الخدمة")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.staff_id.name
    class Meta:
        verbose_name = "نسبة الموظف"  # Singular name
        verbose_name_plural = "نسب الموظفين" # Plural name
        #,verbose_name="القسم"