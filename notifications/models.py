from django.db import models
from datetime import datetime
# Create your models here.
class Notification (models.Model):
    staff_id=models.ForeignKey(Staff,related_name="NotificationStaff",on_delete=models.CASCADE)
    title=models.CharField(max_length=200 )
    content=models.CharField(max_length=200 )
    isRead=models.BooleanField(default=False)
    ndate=models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.staff_id.name +"  "+self.title