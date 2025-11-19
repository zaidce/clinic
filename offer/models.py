from django.db import models
from datetime import datetime

from service.models import Service
# Create your models here.
class Offer(models.Model):
    service_id=models.ForeignKey(Service,related_name="OfferService",on_delete=models.CASCADE,verbose_name="الخدمة")
    newPrice=models.IntegerField(default=0,verbose_name="سعر العرض")
    startDate=models.DateField(default=datetime.now,verbose_name="تاريخ البدء")
    endDate=models.DateField(default=datetime.now,verbose_name="تاريخ الانتهاء")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.service_id.name  +"  "+ str(self.newPrice)
    class Meta:
        verbose_name = "عرض"  # Singular name
        verbose_name_plural = "عروضات" # Plural name
        #,verbose_name="القسم"