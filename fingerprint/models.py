from django.db import models
from datetime import datetime
from staff.models import Staff
import random
import string
# Create your models here.
class FingerPrintMdl(models.Model):
    def generate_random_string(length=10):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for i in range(length))
    staff_id=models.ForeignKey(Staff,on_delete=models.DO_NOTHING,null=True,blank=True,verbose_name="الموظف")
    barcode=models.CharField(max_length=32,default=generate_random_string,verbose_name="باركود")
    fdate=models.DateField(default=datetime.now,verbose_name="التاريخ")
    timeRecord=models.TimeField(null=True,blank=True,verbose_name="الوقت")
    in_out=models.BooleanField(default=True,verbose_name="دخول/خروج")
    def __str__(self):
        if self.staff_id!=None:
            return self.staff_id.name
        return "انتظار"
 

    def nameDisplay(self):
        if self.staff_id.name!=None:
            return self.staff_id.name
        return "انتظار"
    #genderDisplay.str = "ذكر"
    nameadmin = property(nameDisplay)
    # def __str__(self):
    #     if self.user_id.name!=None:
    #         return self.user_id.name
    #    
    #  return "انتظار"
    class Meta:
        verbose_name = "بصمة"  # Singular name
        verbose_name_plural = "بصمة الحضور والانصراف" # Plural name
        #,verbose_name="القسم"