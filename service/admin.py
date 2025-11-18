from django.contrib import admin

from . import models
# Register your models here.
class ServiceDisplay(admin.ModelAdmin):
         list_display = ('id', 'name', 'cost', 'price','points' ) # Add desired fields here
         search_fields = ['name', ]
admin.site.register(models.Service,ServiceDisplay)