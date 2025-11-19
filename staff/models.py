from django.db import models
from datetime import datetime
# Create your models here.
class Staff(models.Model):
    name=models.CharField(max_length=200,verbose_name="الاسم")
    job=models.CharField(max_length=200,blank=True,null=True,verbose_name="المهنة")
    address=models.CharField(max_length=200,blank=True,null=True,verbose_name="العنوان")
    phone=models.CharField(max_length=200,blank=True,null=True,verbose_name="الهاتف")
    specialize=models.CharField(max_length=200,blank=True,null=True,verbose_name="التخصص")
    salary=models.IntegerField(default=0,verbose_name="الراتب")
    isBanned=models.BooleanField(default=False,verbose_name="محظور")
    isAdmin=models.BooleanField(default=False,verbose_name="مسؤول")
    username=models.CharField(max_length=200,blank=True,null=True,verbose_name="المستخدم")
    password=models.CharField(max_length=200,blank=True,null=True,verbose_name="كلمة المرور")
    totalPercent=models.IntegerField(default=0,verbose_name="النسبة")
    nextPercent=models.IntegerField(default=0,verbose_name="النسبة بعد مبلغ العتبة")
    amountThreshold=models.IntegerField(default=0,verbose_name="مبلغ العتبة")
    startDate=models.DateField(default=datetime.now,verbose_name="تاريخ البدء")
    endDate=models.DateField(default=datetime.now,verbose_name="تاريخ الانتهاء")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "موظف"  # Singular name
        verbose_name_plural = "الموظفين" # Plural name
        #,verbose_name="القسم"