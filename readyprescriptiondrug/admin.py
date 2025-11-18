from django.contrib import admin

from . import models
# Register your models here.
class ReadyPrescriptionDrugDisplay(admin.ModelAdmin):
         list_display = ('id', 'readyPrescription_id__name', 'drug_id__name' ) # Add desired fields here
         search_fields = ['readyPrescription_id__name']
admin.site.register(models.ReadyPrescriptionDrug,ReadyPrescriptionDrugDisplay)