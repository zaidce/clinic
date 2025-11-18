from django.db import models
from datetime import datetime

from client.models import Client
from service.models import Service
# Create your models here.
class Sessionx(models.Model):
    choices={
        ('انتظار','انتظار'),
        ('دفع مسبق','دفع مسبق'),
        ('تمت الجلسة','تمت الجلسة'),
    }
    client_id=models.ForeignKey(Client,related_name="SessionxClient",on_delete=models.CASCADE )
    staff_id=models.ForeignKey(Staff,related_name="SessionxStaff",on_delete=models.CASCADE )
    sessionDate=models.DateTimeField(default=datetime.now)
    service_id=models.ForeignKey(Service,related_name="SessionxService",on_delete=models.CASCADE )
    price=models.IntegerField(default=0)
    discount=models.IntegerField(default=0)
    discountPrice=models.IntegerField(default=0)
    newPrice=models.IntegerField(default=0)
    diagnosis=models.CharField(max_length=200,blank=True,null=True)
    sessionState=models.CharField(max_length=200,choices=choices,default='انتظار')
    deviceConsumption=models.IntegerField(default=0)
       #//	-----totalPrice =newPrice+ drugout   
    paied =models.IntegerField(default=0)#//   ------ if true she paid all if false add to creditor
    nextSession=models.BooleanField(default=False) #//(false)
    nextSessionDate=models.DateField(default=datetime.now)
    nextSessionNote=models.CharField(max_length=200,blank=True,null=True)
    deleteRequest=models.BooleanField(default=False) #//[false]
    deleteNote=models.CharField(max_length=200 ,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.client_id.name+"   "+self.service_id.name