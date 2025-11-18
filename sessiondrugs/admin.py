from django.contrib import admin

# Register your models here.
from . import models
# Register your models here.
class SessionDrugDisplay(admin.ModelAdmin):
         list_display = ('id', 'session_id__name', 'drug_id' ) # Add desired fields here
         search_fields = ['session_id__name', 'drug_id' ]
admin.site.register(models.SessionDrug,SessionDrugDisplay)