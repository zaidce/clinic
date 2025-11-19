from django.contrib import admin

from debtordetails import models
# Register your models here.
class DebtorDetailDisplay(admin.ModelAdmin):
         list_display = ('id','xxx', 'amount', 'debtorDetailDate','note'   ) # Add desired fields here
         @admin.display(description="المدين") # Set the column header here
         def xxx(self, obj):
                return obj.debtor_id.client_id.name
admin.site.register(models.DebtorDetail,DebtorDetailDisplay)