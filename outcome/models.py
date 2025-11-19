from django.db import models
from datetime import datetime
# Create your models here.
class Outcome(models.Model):
    outcomeDate=models.DateField(default=datetime.now,verbose_name="التاريخ")
    outcomeType=models.CharField(max_length=200,verbose_name="نوع المصروفات")
    name=models.CharField(max_length=200,verbose_name="الاسم")
    total=models.IntegerField( verbose_name="المبلغ")
    note=models.CharField(max_length=200,blank=True,null=True,verbose_name="الملاحظات")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "مصروف"  # Singular name
        verbose_name_plural = "المصروفات" # Plural name
        #,verbose_name="القسم"