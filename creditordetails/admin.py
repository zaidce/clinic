from django.contrib import admin
from creditordetails import models
# Register your models here.
class CreditorDetailsDisplay(admin.ModelAdmin):
         list_display = ('id', 'amount', 'creditorDetailsDate',  ) # Add desired fields here
 
admin.site.register(models.CreditorDetails,CreditorDetailsDisplay)