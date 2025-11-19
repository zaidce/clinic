from django.db import models
from datetime import datetime

from staff.models import Staff
# Create your models here.
class Notification (models.Model):
    staff_id=models.ForeignKey(Staff,related_name="NotificationStaff",on_delete=models.CASCADE,verbose_name="الموظف")
    title=models.CharField(max_length=200,verbose_name="العنوان" )
    content=models.CharField(max_length=200 ,verbose_name="المحتوى")
    isRead=models.BooleanField(default=False,verbose_name="تمت القراءة")
    ndate=models.DateTimeField(default=datetime.now,verbose_name="التاريخ")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.staff_id.name +"  "+self.title
    class Meta:
        verbose_name = "اشعار"  # Singular name
        verbose_name_plural = "الاشعارات" # Plural name
        #,verbose_name="القسم"