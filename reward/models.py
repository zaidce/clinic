from django.db import models
from datetime import datetime

from staff.models import Staff
# Create your models here.
class Reward(models.Model):
    staff_id=models.ForeignKey(Staff,related_name="RewardStaff",on_delete=models.CASCADE,verbose_name="الموظف")
    gift=models.IntegerField( verbose_name="المبلغ")
    reason=models.CharField(max_length=200,blank=True,null=True,verbose_name="السبب")
    rewardDate=models.DateTimeField(default=datetime.now,verbose_name="التاريخ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.staff_id.name+ "  "+ self.gift
    class Meta:
        verbose_name = "مكافئة"  # Singular name
        verbose_name_plural = "المكافئات" # Plural name
        #,verbose_name="القسم"