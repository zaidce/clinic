from django.contrib import admin

from . import models
# Register your models here.
class StaffServicPercentDisplay(admin.ModelAdmin):
         list_display = ('id', 'staff_id__name', 'service_id__name', 'percent' ) # Add desired fields here
         search_fields = ['staff_id__name', 'service_id__name']
admin.site.register(models.StaffServicPercent,StaffServicPercentDisplay)