from django.contrib import admin

# Register your models here.
from . import models
# Register your models here.
class DrugDisplay(admin.ModelAdmin):
         list_display = ('id', 'name', 'dose', ) # Add desired fields here
         search_fields = ['name', ]
admin.site.register(models.Drug,DrugDisplay)