from django.db import models
from datetime import datetime

from drug.models import Drug
from readyprescription.models import ReadyPrescription
# Create your models here.
class ReadyPrescriptionDrug(models.Model):
    readyPrescription_id=models.ForeignKey(ReadyPrescription,related_name="ReadyPrescriptionDrugReadyPrescription",on_delete=models.CASCADE,verbose_name="الوصفة")
    drug_id=models.ForeignKey(Drug,related_name="ReadyPrescriptionDrugDrug",on_delete=models.CASCADE,verbose_name="الدواء")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.readyPrescription_id.name + "    "+self.drug_id.name
    class Meta:
        verbose_name = "دواء الوصفة"  # Singular name
        verbose_name_plural = "ادوية الوصفات الجاهزة" # Plural name
        #,verbose_name="القسم"