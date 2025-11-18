from django.contrib import admin

from debtordetails import models
# Register your models here.
class DebtorDetailDisplay(admin.ModelAdmin):
         list_display = ('id', 'amount', 'debtorDetailDate',  ) # Add desired fields here
 
admin.site.register(models.DebtorDetail,DebtorDetailDisplay)