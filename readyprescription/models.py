from django.db import models
from datetime import datetime
# Create your models here.
class ReadyPrescription(models.Model):
    name=models.CharField(max_length=200,verbose_name="الوصفة" )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "وصفة جاهزة"  # Singular name
        verbose_name_plural = "الوصفات الجاهزة" # Plural name
        #,verbose_name="القسم"