from django.contrib import admin

# Register your models here.

 
from . import models
# Register your models here.
class DebtorDisplay(admin.ModelAdmin):
         list_display = ('id', 'client_id__name', 'total', 'DebtorDate' ) # Add desired fields here
         search_fields = ['client_id__name', 'total', 'DebtorDate']
admin.site.register(models.Debtor,DebtorDisplay)