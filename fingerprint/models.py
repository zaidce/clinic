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
    staff_id=models.ForeignKey(Staff,on_delete=models.DO_NOTHING,null=True,blank=True)
    barcode=models.CharField(max_length=32,default=generate_random_string)
    fdate=models.DateField(default=datetime.now)
    timeRecord=models.TimeField(null=True,blank=True)
    in_out=models.BooleanField(default=True)
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
    #     return "انتظار"