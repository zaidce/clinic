from django.contrib import admin

from . import models
# Register your models here.
class PunishmentDisplay(admin.ModelAdmin):
         list_display = ('id', 'staff_id__name', 'cost', 'isDone' ,'punishmentDate') # Add desired fields here
         search_fields = ['staff_id__name' ]
admin.site.register(models.Punishment,PunishmentDisplay)