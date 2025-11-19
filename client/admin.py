from django.contrib import admin

from client import models

# Register your models here.
class ClientDisplay(admin.ModelAdmin):
         list_display = ('id', 'name', 'bornYear', 'phone','gender' ) # Add desired fields here
         search_fields = ['name', 'bornYear', 'phone']
admin.site.register(models.Client,ClientDisplay)