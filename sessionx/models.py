from django.db import models
from datetime import datetime

from client.models import Client
from service.models import Service
from staff.models import Staff
# Create your models here.
class Sessionx(models.Model):
    choices={
        ('انتظار','انتظار'),
        ('دفع مسبق','دفع مسبق'),
        ('تمت الجلسة','تمت الجلسة'),
    }
    client_id=models.ForeignKey(Client,related_name="SessionxClient",on_delete=models.CASCADE ,verbose_name="الزبون")
    staff_id=models.ForeignKey(Staff,related_name="SessionxStaff",on_delete=models.CASCADE,verbose_name="الموظف" )
    sessionDate=models.DateTimeField(default=datetime.now,verbose_name="تاريخ الجلسة")
    service_id=models.ForeignKey(Service,related_name="SessionxService",on_delete=models.CASCADE,verbose_name="الخدمة" )
    price=models.IntegerField(default=0,verbose_name="المبلغ")
    discount=models.IntegerField(default=0,verbose_name="نسبة الخصم")
    discountPrice=models.IntegerField(default=0,verbose_name="مبلغ الخصم")
    newPrice=models.IntegerField(default=0,verbose_name="السعر بعد الخصم")
    diagnosis=models.CharField(max_length=200,blank=True,null=True,verbose_name="التشخيص")
    sessionState=models.CharField(max_length=200,choices=choices,default='انتظار',verbose_name="حالة الجلسة")
    deviceConsumption=models.IntegerField(default=0,verbose_name="استهلاك الجهاز")
       #//	-----totalPrice =newPrice+ drugout   
    paied =models.IntegerField(default=0,verbose_name="المدفوع")#//   ------ if true she paid all if false add to creditor
    nextSession=models.BooleanField(default=False,verbose_name="جلسة قادمة؟") #//(false)
    nextSessionDate=models.DateField(default=datetime.now,verbose_name="تاريخ الجلسة القادمة")
    nextSessionNote=models.CharField(max_length=200,blank=True,null=True,verbose_name="ملاحظات الجلسة القادمة")
    deleteRequest=models.BooleanField(default=False,verbose_name="طلب الحذف") #//[false]
    deleteNote=models.CharField(max_length=200 ,verbose_name="سبب الحذف")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.client_id.name+"   "+self.service_id.name
    class Meta:
        verbose_name = "جلسة"  # Singular name
        verbose_name_plural = "الجلسات" # Plural name
        #,verbose_name="القسم"