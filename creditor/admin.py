from django.contrib import admin

 
from . import models
# Register your models here.
class CreditorDisplay(admin.ModelAdmin):
         list_display = ('id', 'client_id__name', 'total', 'creditorDate' ) # Add desired fields here
         search_fields = ['client_id__name', 'total', 'creditorDate']
admin.site.register(models.Creditor,CreditorDisplay)