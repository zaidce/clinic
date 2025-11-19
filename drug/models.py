from django.db import models
from datetime import datetime
# Create your models here.
class Drug(models.Model):
    name=models.CharField(max_length=200,verbose_name="الاسم")
    dose=models.CharField(max_length=200,blank=True,null=True,verbose_name="الجرعة")
    days=models.IntegerField(default=0,blank=True,null=True,verbose_name="عدد الايام")
    times=models.IntegerField(default=0,blank=True,null=True,verbose_name="مرة كل يوم")
    note=models.CharField(max_length=200,blank=True,null=True,verbose_name="الملاحظات")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name = "دواء"  # Singular name
        verbose_name_plural = "الادوية" # Plural name
        #,verbose_name="القسم" 