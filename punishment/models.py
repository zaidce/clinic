from django.db import models
from datetime import datetime

from staff.models import Staff
# Create your models here.
class Punishment(models.Model):
    staff_id=models.ForeignKey(Staff,related_name="PunishmentStaff",on_delete=models.CASCADE)
    cost=models.IntegerField(default=0)
    reasone=models.CharField(max_length=200 )
    isDone=models.BooleanField(default=False)
    punishmentDate=models.DateField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.staff_id.name