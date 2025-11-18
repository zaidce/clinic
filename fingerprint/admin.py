from django.contrib import admin

from . import models
# Register your models here.
class FingerPrintMdlDisplay(admin.ModelAdmin):
         list_display = ('id', 'staff_id__name','fdate', 'timeRecord','in_out' ) # Add desired fields here
         search_fields = [ 'staff_id__name',]
admin.site.register(models.FingerPrintMdl,FingerPrintMdlDisplay)