from django.contrib import admin

# Register your models here.

 
from . import models
# Register your models here.
class DebtorDisplay(admin.ModelAdmin):
         list_display = ('id', 'xxx', 'total', 'DebtorDate','note' ) # Add desired fields here
         search_fields = ['client_id__name', 'total', 'DebtorDate']
         @admin.display(description="الزبون") # Set the column header here
         def xxx(self, obj):
                return obj.client_id.name
admin.site.register(models.Debtor,DebtorDisplay) 