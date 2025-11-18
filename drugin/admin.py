from django.contrib import admin

from . import models
# Register your models here.
class DruginDisplay(admin.ModelAdmin):
         list_display = ('id', 'staff_id__name', 'name', 'quantity','minLevel','entryDate' ,'expireDate') # Add desired fields here
         search_fields = ['name']
admin.site.register(models.Drugin,DruginDisplay)