from django.contrib import admin

from . import models
# Register your models here.
class DrugoutDisplay(admin.ModelAdmin):
         list_display = ('id', 'drugin_id__name', 'staff_id__name', 'quantity','outDate' ) # Add desired fields here
         search_fields = ['drugin_id__name', 'staff_id__name', 'outDate']
         @admin.display(description="الدواء المدخل") # Set the column header here
         def xxx(self, obj):
                return obj.drugin_id.name
admin.site.register(models.Drugout,DrugoutDisplay) 