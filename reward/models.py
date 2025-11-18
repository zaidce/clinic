from django.db import models
from datetime import datetime

from staff.models import Staff
# Create your models here.
class Reward(models.Model):
    staff_id=models.ForeignKey(Staff,related_name="RewardStaff",on_delete=models.CASCADE)
    gift=models.IntegerField(default=0)
    reason=models.CharField(max_length=200,blank=True,null=True)
    rewardDate=models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.staff_id.name+ "  "+ self.gift