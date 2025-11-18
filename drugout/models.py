from django.db import models
from datetime import datetime

from drugin.models import Drugin
# Create your models here.
class Drugout(models.Model):
    drugin_id=models.ForeignKey(Drugin,related_name="DrugoutDrugin",on_delete=models.CASCADE)
    staff_id=models.ForeignKey(Staff,related_name="DrugoutStaff",on_delete=models.CASCADE)
    session_id=models.ForeignKey(Sessionx,related_name="DrugoutSessionx",on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0)
    outDate=models.DateTimeField(default=datetime.now)
    note=models.CharField(max_length=200,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.drugin_id.name