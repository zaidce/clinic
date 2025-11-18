from django.db import models

from service.models import Service
class StaffServicPercent(models.Model):
    staff_id=models.ForeignKey(Staff,related_name="StaffServicPercentStaff" )
    service_id=models.ForeignKey(Service,related_name="StaffServicPercentService" )
    percent=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.staff_id.name