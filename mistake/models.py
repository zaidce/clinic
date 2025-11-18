from django.db import models
from datetime import datetime
class Mistake(models.Model):
    staff_id=models.ForeignKey(Staff,related_name="MistakeStaff",on_delete=models.CASCADE)
    func=models.CharField(max_length=200,blank=True,null=True)
    detail=models.CharField(max_length=200,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.func