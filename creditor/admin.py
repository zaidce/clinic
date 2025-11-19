from django.contrib import admin

 
from . import models
# Register your models here.
class CreditorDisplay(admin.ModelAdmin):
         list_display = ('id', 'xxx', 'total', 'creditorDate','note' ) # Add desired fields here
         search_fields = ['client_id__name', 'total', 'creditorDate']
         @admin.display(description="الزبون") # Set the column header here
         def xxx(self, obj):
                return obj.client_id.name
admin.site.register(models.Creditor,CreditorDisplay)