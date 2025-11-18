from django.db import models

from service.models import Service
from staff.models import Staff
class StaffServicPercent(models.Model):
    staff_id=models.ForeignKey(Staff,related_name="StaffServicPercentStaff",on_delete=models.CASCADE )
    service_id=models.ForeignKey(Service,related_name="StaffServicPercentService",on_delete=models.CASCADE )
    percent=models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.staff_id.name