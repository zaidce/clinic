from django.contrib import admin
from creditordetails import models
# Register your models here.
class CreditorDetailsDisplay(admin.ModelAdmin):
         list_display = ('id','xxx', 'amount', 'creditorDetailsDate','note'  ) # Add desired fields here
         @admin.display(description="الدائن") # Set the column header here
         def xxx(self, obj):
                return obj.creditor_id.client_id.name
admin.site.register(models.CreditorDetails,CreditorDetailsDisplay)