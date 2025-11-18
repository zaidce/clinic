from django.db import models
from datetime import datetime
# Create your models here.
class Offer(models.Model):
    service_id=models.ForeignKey(Service,related_name="OfferService",on_delete=models.CASCADE)
    newPrice=models.IntegerField(default=0)
    startDate=models.DateTimeField(default=datetime.now)
    endDate=models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.service_id.name  +"  "+ str(self.newPrice)